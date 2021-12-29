from app.core.error_success_result import ErrorResult
from pymongo import MongoClient


class MongodbLogConnector:
    def connect_log(self):
        client = MongoClient('mongodb://127.0.0.1:27017/')
        mydb = client['log_db']
        return mydb['log']
        
    def connect_exception_log(self):
        client = MongoClient('mongodb://127.0.0.1:27017/')
        mydb = client['log_db']
        return mydb['exception_error_log']
    