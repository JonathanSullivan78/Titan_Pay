from src.accounting.payment_method import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, full_name, full_address, total_pay):
        PaymentMethod.__init__(self)
        self.__full_name = full_name
        self.__full_address = full_address
        self.__total_pay = total_pay

    def pay(self):
        output = "Mailing a check to " + self.__full_name + " for $" + str(format(self.__total_pay, ',.2f')) + " to " + self.__full_address
        return output