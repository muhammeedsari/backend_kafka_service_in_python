from app.core.error_success_data_result import ErrorDataResult
from app.helpers.mogodb_customer_connector import MongodbCustomerConnector
import simplejson as json

class CreditCardCustomerDal:

    def insert_data_customer(self, data:json):
        mongodb_collection = MongodbCustomerConnector()
        connect_customer = mongodb_collection.connect_customers()
        connect_customer.insert_one(data)





