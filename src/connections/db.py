from asynch import connect, connection
from asynch.cursors import DictCursor
from typing import Annotated
from fastapi import Depends
import json
from datetime import datetime

import aiocache


from config import settings
from src.connections.cache_config import redis_connection as cache_redis

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Thank you to https://github.com/gotsalyuk/fastapi-clickhouse/blob/main/db.py
class ClickHouse:
    @classmethod
    async def create_db(cls, db_name: str) -> bool:
        """Create clickhouse db on first run

        Args:
            db_name (str): name of db
        Returns:
            bool: result
        """
        conn = await connect(
            host=settings.ch_host,
            port=settings.ch_port,
        )
        async with conn.cursor(cursor=DictCursor) as cursor:
            result = await cursor.execute(query=f"create database if not exists {db_name};")
        await conn.close()

        if result:
            return True
        return False

    
    @classmethod
    async def conn(cls,) -> connection.Connection:
        """ click house connection

        Returns:
            connection.Connection: Connection
        """
        return await connect(
            host=settings.ch_host,
            port=settings.ch_port,
            database=settings.ch_db,
            user=settings.ch_user,
            password=settings.ch_pass
        )

    @classmethod
    async def execute_sql(cls, query) -> bool:
        """execute sql

        Args:
            query (_type_): sql query
        Returns:
            bool: result
        """
        conn = await cls.conn()
        async with conn.cursor(cursor=DictCursor) as cursor:
            result = await cursor.execute(query)
        await conn.close()

        if result:
            return True
        return False


    @classmethod
    async def fetchall(cls, query: str, params: dict = {}) -> list:
        """ get many records

        Args:
            query (str): sql query
            params (dict, optional): query params. Defaults to None.
        Returns:
            list: record dict
        """
        cache_key = f'data:{hash(f"{query}:{params}")}'
        cache = await cache_redis.get(cache_key)
        if cache:
            cache_data = json.loads(cache)
            if cache_data:
                return cache_data
            else:
                return None 
        
        conn = await cls.conn()
        async with conn.cursor(cursor=DictCursor) as cursor:
            await cursor.execute(query, params)
            ret = await cursor.fetchall()
        await conn.close()
        
        # Only cache if there is data
        if ret:
            await cache_redis.set(cache_key, json.dumps(ret, cls=DateTimeEncoder), ttl=1800) # 30 minutes
            return ret
        else:
            return None

    @classmethod
    async def fetchone(cls, query: str, params: dict = {}) -> dict:
        """ get one record

        Args:
            query (str): sql query
            params (dict, optional): query params. Defaults to None.

        Returns:
            dict: record
        """
        cache_key = f'data:{hash(f"{query}:{params}")}'
        cache = await cache_redis.get(cache_key)
        if cache:
            return json.loads(cache)
        
        conn = await cls.conn()
        async with conn.cursor(cursor=DictCursor) as cursor:
            await cursor.execute(query, params)
            ret = await cursor.fetchone()
        await conn.close()
        
        await cache_redis.set(cache_key, json.dumps(ret, cls=DateTimeEncoder), ttl=1800) # 30 minutes
        
        return ret

    @classmethod
    async def insert_many(cls, table: str, values: list) -> bool:
        """ insert_many records

        Args:
            table (str): table name

            values (list): dicts

        Returns:
            bool: insert result
        """
        insert_fields = ','.join([i for i in values[0].keys()])
        conn = await cls.conn()
        async with conn.cursor(cursor=DictCursor) as cursor:
            result = await cursor.execute(
                f"""INSERT INTO {table} ({insert_fields}) VALUES """, values
            )
        await conn.close()
        if result:
            return True
        return False


    @classmethod
    async def check_connection_to_click_house(cls) -> bool:
        """ check click house is alive

        Returns:
            bool: flag_connected
        """
        try:
            conn = await cls.conn()
            flag_connected = conn.connected
            await conn.close()
            return flag_connected
        except Exception as e:
            print(e, flush=True)
            return False





async def get_clickhouse():
    ch = ClickHouse()
    return ch

ClickhouseConn = Annotated[ClickHouse, Depends(get_clickhouse)]

