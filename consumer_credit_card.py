from app.core.error_success_data_result import ErrorDataResult
from app.core.error_success_result import ErrorResult
from app.helpers.mongodb_log_connector import MongodbLogConnector
from app.helpers.mogodb_customer_connector import MongodbCustomerConnector
from app.controller.credit_card_controller import CreditCardController


mongodb_connector = MongodbCustomerConnector()
mongodb_connector.connect_customers()

mongodb_connector = MongodbLogConnector()
mongodb_connector.connect_log()

credit_card_controller = CreditCardController()
credit_card_controller.create_credit_card_customer()

# credit_card_controller.create_credit_card_log()
