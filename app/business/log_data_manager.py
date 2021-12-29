from app.core.error_success_data_result import ErrorDataResult
from app.core.messages import Messages
from app.models.log_model import LogModel
from app.models.credit_card_model import CreditCardModel
from app.dataAccess.log_data_dal import LogDataDal
import simplejson as json
from datetime import datetime



class LogDataManager:

    def __init__(self):
        self.log_data_dal = LogDataDal()
        
    def create_log(self, log_type, userId, action, message):
        try:
            information = f"userID={userId}, action={action}, message={message}"
            log_info_model = LogModel(log_type=log_type,
                                                created_at=str(
                                                    datetime.now()),
                                                information=information)

            log_model_dict = log_info_model.__dict__
            jsonStr = json.dumps(log_model_dict)
            self.insert_log(log_model_dict)
            print(jsonStr)
        except Exception as err:
            return ErrorDataResult(message=err.__doc__)



   
    def insert_log(self, data):
        try:
            self.log_data_dal.insert_data_log(data)
        except Exception as err:
            return ErrorDataResult(message=err.__doc__)

