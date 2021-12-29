from app.core.error_success_result import ErrorResult
from pymongo import MongoClient


class MongodbCustomerConnector:
    def connect_customers(self):
        try:
            client = MongoClient('mongodb://127.0.0.1:27017/')
            mydb = client['customer_db']
            return mydb['customer']
        except Exception as err:
            return ErrorResult(message=err.__doc__)
