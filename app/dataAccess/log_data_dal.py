from app.core.error_success_data_result import ErrorDataResult
from app.helpers.mongodb_log_connector import MongodbLogConnector
import simplejson as json

class LogDataDal:

    def insert_data_log(self, data:json):
        mongodb_collection = MongodbLogConnector()
        connector_log = mongodb_collection.connect_log()
        connector_log.insert_one(data)
        
    def insert_exception_log(self, data: json):
        mongodb_collection = MongodbLogConnector()
        connector_log = mongodb_collection.connect_exception_log()
        connector_log.insert_one(data)
