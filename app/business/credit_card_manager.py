from app.core.log_types import LogTypes
from app.core.messages import Messages
from app.core.error_success_result import ErrorResult, SuccessResult
from app.core.error_success_data_result import ErrorDataResult, SuccessDataResult
from app.business.log_data_manager import LogDataManager
from app.dataAccess.credit_card_customer_dal import CreditCardCustomerDal


class CreditCardManager:

    def __init__(self):
        self.credit_card_dal = CreditCardCustomerDal()
        self.log_data_manager = LogDataManager()

    def detect_customer(self, json_data1):
        try:
            self.control_remaining_installments(json_data1)

            self.control_minimum_payment_amount(json_data1)

            self.control_overdue_installment_debt(json_data1)
            
            if (json_data1["remain_limit"] < json_data1["product_price"]):
                self.log_data_manager.create_error_log_remain_limit(json_data1)
                return ErrorResult(message=Messages.log_installment_error_message)


            self.create_customer(json_data1)
            print(json_data1)


        except Exception as err:          
            self.log_data_manager.create_log(log_type=LogTypes.exception_log,
                                             userId=json_data1["userId"],
                                             action="create_customer",
                                             message=err.__doc__)
            return ErrorResult(message=Messages.error_message)

    def control_overdue_installment_debt(self, json_data1):
        if (json_data1["overdue_installment_debt"] == 1):
            self.log_data_manager.create_log(log_type=LogTypes.warning_log, 
                                             userId=json_data1["userId"],
                                             action="create_customer",
                                             message=Messages.log_installment_warning_message)
            

#ToDO Refactor edilecek    
           
    def control_minimum_payment_amount(self, json_data1):
        if (json_data1["minimum_payment_amount"] < json_data1["amount_of_debt"]*20/100):
            self.log_data_manager.log_warning_minimum_payment_amount(
                    json_data1)

    def control_remaining_installments(self, json_data1):
        if (json_data1["remaining_installments"] == 0):
            self.log_data_manager.log_warning_remaining_installments(
                    json_data1)

    def create_customer(self, data):
        try:
            self.credit_card_dal.insert_data_customer(data)
            return SuccessResult()
        except Exception as err:
            return ErrorResult(message=err.__doc__)


# ToDO Verinin yapısallığının kontrolüne validasyon denir.
# ** Veri boş gelebilir, Veri yanlış bir tipte gelebilir
# ? Verinin istenilen aralıklardan büyük veya küçük gelebilir.
# ** Validasyon örneği : karakter sayısı, formatı
#! İş katmanı validasyon ve iş kurallarını,
#! loglama, cacheleme, kod hatlarını yakalama exception handling barındırır
# ? İş kuralları örnek : Maximum bir kategoride 100 farklı ürün olabilir
# ToDO Tüm işler ayrı fonksiyon olur. İş kuralları private fonksiyon olur.
# * Tüm bu fonksiyonlar manager class'ının içinde yer alır.
# ? Fakat ortak kullanılabilecek belli başlı iş yükleri helper içinde yer alabilir.
#! Bir tabloyu ilgilendiren Manager yalnızca kendi ile ilgili olan DataAccessLayer'ını çağırabilir.
#! Bu sayede proje microservice'lere bölünebilmektedir.
#! Fakat bir manager başka bir manager'i çağırabilir. Bu manager'in çıktılarını kullanabilir.
