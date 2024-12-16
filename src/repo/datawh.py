from src.connections.db import ClickHouse

class DataWH:
    def __init__(self, db: ClickHouse):
        self.db = db

    def get_data(self):
        return self.db.get_data()