from src.accounting.payment_method import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, first_name, last_name, total_pay):
        PaymentMethod.__init__(self, first_name, last_name)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__total_pay = total_pay

    def pay(self, first_name, last_name, total_pay):
        return "A check for $" + total_pay+ "is waiting for " + first_name + " " + last_name + " at the PostMaster."