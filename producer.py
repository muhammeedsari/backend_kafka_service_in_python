from app.controller.produce_controller import ProduceController

producer = ProduceController()

while True:
    producer.produce_credit_card_customer()
