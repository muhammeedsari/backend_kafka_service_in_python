class CreditCardModel:
    def __init__(self, userId, name,  job, current_location,  
    last_payment_date_month, last_payment_date_day, gender, credit_card_number, 
    credit_card_security_code, credit_card_expire_date, amount_of_debt, remain_limit,
    minimum_payment_amount, remaining_installments, overdue_installment_debt, product_price):
        self.userId = userId
        self.name = name
        self.job = job
        self.current_location = current_location  
        self.last_payment_date_month = last_payment_date_month
        self.last_payment_date_day = last_payment_date_day
        self.gender = gender
        self.credit_card_number = credit_card_number
        self.credit_card_security_code = credit_card_security_code
        self.credit_card_expire_date = credit_card_expire_date
        self.amount_of_debt = amount_of_debt
        self.remain_limit = remain_limit
        self.minimum_payment_amount = minimum_payment_amount
        self.remaining_installments = remaining_installments
        self.overdue_installment_debt = overdue_installment_debt
        self.product_price = product_price


