import os
from typing import List
from src.connections.cache_config import cachefunc, redis_client
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
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_drivers(self):
        query = self._read_query('drivers', 'drivers_info.sql')
        return await self.db.fetchall(query)
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_info(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_info.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_wins(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_wins.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_events(self, cust_id: int, pagination: Pagination) -> dict:
        query = self._read_query('drivers', 'driver_events.sql')
        return await self.db.fetchall(query, {
            'cust_id': cust_id,
            'limit': pagination.limit,
            'offset': pagination.offset
            })
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_rival(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_rival.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def search_driver(self, search_term: str, pagination: Pagination) -> dict:
        query = self._read_query('drivers', 'driver_search.sql')
        return await self.db.fetchall(query, {
            'search_term': f'%{search_term}%',
            'limit': pagination.limit,
            'offset': pagination.offset
            })
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour    
    async def get_driver_winrate_by_category(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_winrate_by_category.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_winrate(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_winrate.sql')
        return await self.db.fetchone(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def get_driver_irating(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_irating.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def driver_stats_rollup_by_season(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_stats_rollup_by_season.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def driver_track_stats(self, cust_id: int) -> dict:
        query = self._read_query('drivers', 'driver_track_statistics.sql')
        return await self.db.fetchall(query, {'cust_id': cust_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def top_drivers_by_wins_this_season(self, limit=10) -> List[dict]:
        query = self._read_query('drivers', 'top_drivers_by_wins_this_season.sql')
        return await self.db.fetchall(query, {'limit': limit})
    
    ###############################
    # Session related queries     #
    ###############################
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def session_info(self, subsession_id: int) -> dict:
        query = self._read_query('sessions', 'session_info.sql')
        return await self.db.fetchone(query, {'subsession_id': subsession_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def session_results(self, subsession_id: int) -> dict:
        query = self._read_query('sessions', 'session_race_results.sql')
        return await self.db.fetchall(query, {'subsession_id': subsession_id})
    
    ###############################
    # iRating related queries     #
    ###############################
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def irating_filters(self) -> dict:
        query = self._read_query('irating', 'irating_filters.sql')
        return await self.db.fetchall(query)
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def irating_distribution(self, license: str = 'Sports Car', year: int = 2025, quarter: int = 1) -> List[dict]:
        query = self._read_query('irating', 'irating_distribution.sql')
        return await self.db.fetchall(query, {
            'license': license,
            'year': year,
            'quarter': quarter
        })
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def irating_distribution_kpis(self, license: str = 'Sports Car', year: int = 2025, quarter: int = 1) -> List[dict]:
        query = self._read_query('irating', 'irating_distribution_kpis.sql')
        return await self.db.fetchone(query, {
            'license': license,
            'year': year,
            'quarter': quarter
        })
    
    ###############################
    # Series related queries      #
    ###############################
    
    @cachefunc(r=redis_client, ttl=86400) # 1 day
    async def max_series_year_quarter_by_id(self, series_id: int) -> dict:
        query = self._read_query('series', 'max_season_year_quarter_by_id.sql')
        return await self.db.fetchone(query, {'series_id': series_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def series_this_week_by_participation(self):
        query = self._read_query('series', 'series_by_participation_this_week.sql')
        return await self.db.fetchall(query)
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def lookup_series_seasons_by_id(self, series_id: int) -> List[dict]:
        query = self._read_query('series', 'lookup_series_seasons_by_id.sql')
        return await self.db.fetchall(query, {'series_id': series_id})
    
    @cachefunc(r=redis_client, ttl=3600, skip_first_arg=True) # 1 hour
    async def series_latest_season_participation(self, series_id: int) -> List[dict]:
        query = self._read_query('series', 'series_latest_season_participation.sql')
        return await self.db.fetchall(query, {'series_id': series_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def series_seasons_stats(self, series_id: int) -> List[dict]:
        query = self._read_query('series', 'series_seasons_stats.sql')
        return await self.db.fetchall(query, {'series_id': series_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def series_season_weeks(self, series_id: int, season_id: int) -> List[dict]:
        query = self._read_query('series', 'series_season_weeks.sql')
        return await self.db.fetchall(query, {'series_id': series_id, 'season_id': season_id})
    
    @cachefunc(r=redis_client, ttl=3600) # 1 hour
    async def week_irating_avg(self, season_id: int, week_num: int):
        query = self._read_query('seasons', 'week_irating_avg.sql')
        return await self.db.fetchall(query, {'season_id': season_id, 'race_week': week_num})