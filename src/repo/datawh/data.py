import os
from typing import List
from src.connections.db import ClickHouse
from src.pagination import Pagination

class DataWH:
    def __init__(self, db: ClickHouse):
        self.db = db

    def _read_query(self, subject: str, query_name: str):
        pyfile_path = os.path.dirname(__file__)
        with open(os.path.join(pyfile_path, 'queries', subject, query_name), 'r') as f:
            query = f.read()
        return query
    
    async def get_drivers(self):
        query = self._read_query('drivers', 'drivers_info.sql')
        return await self.db.fetchall(query)
    
    async def get_driver_info(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_info.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    async def get_driver_wins(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_wins.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    async def get_driver_events(self, cust_id: int, pagination: Pagination) -> dict:
        query = self._read_query('drivers', 'driver_events.sql')
        return await self.db.fetchall(query, {
            'cust_id': cust_id,
            'limit': pagination.limit,
            'offset': pagination.offset
            })
    
    async def get_driver_rival(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_rival.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    async def search_driver(self, search_term: str, pagination: Pagination) -> dict:
        query = self._read_query('drivers', 'driver_search.sql')
        return await self.db.fetchall(query, {
            'search_term': f'%{search_term}%',
            'limit': pagination.limit,
            'offset': pagination.offset
            })
        
    async def get_driver_winrate_by_category(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_winrate_by_category.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    async def get_driver_winrate(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_winrate.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    async def get_driver_irating(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_irating.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    async def driver_stats_rollup_by_season(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_stats_rollup_by_season.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    async def driver_track_stats(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_track_statistics.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    async def top_drivers_by_wins_this_season(self, limit=10) -> List[dict]:
        query = self._read_query('drivers', 'top_drivers_by_wins_this_season.sql')
        return await self.db.fetchall(query, {'limit': limit})
    
    ###############################
    # Session related queries     #
    ###############################
    
    async def session_info(self, subsession_id: int) -> dict:
        query = self._read_query('sessions', 'session_info.sql')
        return await self.db.fetchone(query, {'subsession_id': subsession_id})
    
    async def session_results(self, subsession_id: int) -> dict:
        query = self._read_query('sessions', 'session_race_results.sql')
        return await self.db.fetchall(query, {'subsession_id': subsession_id})
    
    ###############################
    # iRating related queries     #
    ###############################
    
    async def irating_filters(self) -> dict:
        query = self._read_query('irating', 'irating_filters.sql')
        return await self.db.fetchone(query)
    
    async def irating_distribution(self, license: str = 'Sports Car', year: int = 2025, quarter: int = 1) -> List[dict]:
        query = self._read_query('irating', 'irating_distribution.sql')
        return await self.db.fetchall(query, {
            'license': license,
            'year': year,
            'quarter': quarter
        })
    
    
