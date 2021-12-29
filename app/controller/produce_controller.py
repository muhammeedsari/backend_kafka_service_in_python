from app.core.kafka import Kafka
from app.core.error_success_data_result import ErrorDataResult
from app.models.credit_card_model import CreditCardModel
from faker import Faker
import simplejson as json
import random
import datetime


class ProduceController:

    def __init__(self):
        self.fake = Faker()
        self.kafka = Kafka()

    def detect_overdue(self):
        overdue_boolean = self.fake.boolean(chance_of_getting_true=28)
        if overdue_boolean == True:
            overdue_installment = 1
        else:
            overdue_installment = 0
        return overdue_installment

    def create_gender(self):
        gender = "Male"
        gender_boolean = self.fake.boolean()
        if gender_boolean == True:
            gender = "Female"
        return gender

    def separate_day_and_month(self):
        format = "%Y-%m-%d"
        input = self.fake.date()
        payment_date = datetime.datetime.strptime(input, format)
        date_month = payment_date.month
        date_day = payment_date.day
        return date_month, date_day

    def produce_credit_card_customer(self):
        try:
            date_month, date_day = self.separate_day_and_month()
            gender = self.create_gender()
            overdue_installment = self.detect_overdue()

            credit_card = CreditCardModel(userId=self.fake.aba(),
                                        name=self.fake.name(),
                                        job=self.fake.job(),
                                        current_location=self.fake.city(),
                                        last_payment_date_month=date_month,
                                        last_payment_date_day=date_day,
                                        gender=gender,
                                        credit_card_number=self.fake.credit_card_number(),
                                        credit_card_security_code=self.fake.credit_card_security_code(),
                                        credit_card_expire_date=self.fake.credit_card_expire(),
                                        amount_of_debt=random.randint(
                                            254, 18976),
                                        remain_limit=random.randint(-18, 42976),
                                        minimum_payment_amount=random.randint(
                                            50, 9876),
                                        remaining_installments=random.randint(
                                            0, 24),
                                        overdue_installment_debt=overdue_installment,
                                        product_price=random.randint(100, 2976))

            credit_card_dict = credit_card.__dict__
            jsonObj = json.dumps(credit_card_dict)

            self.kafka.produce_message(
                topic="credit_card3",
                key="test_key",
                value=jsonObj)
            
        except Exception as err:
            return ErrorDataResult(message=err.__doc__)
            #print("Error:  {}".format(err.__doc__))
