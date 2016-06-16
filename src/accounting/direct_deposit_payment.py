from src.accounting.payment_method import PaymentMethod

class DirectDepositPayment(PaymentMethod):
    def __init__(self, first_name, last_name, total_pay, bank_name, routing_number, account_id):
        PaymentMethod.__init__(self, first_name, last_name)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__total_pay = total_pay
        self.__bank_name = bank_name
        self.__routing_number = routing_number
        self.__account_id = account_id

    def pay(self, total_pay, bank_name, routing_number, account_id):
        return "Depositing $" + total_pay+ "in " + bank_name + " Account Number: " + account_id + " using Routing Number: " + routing_number