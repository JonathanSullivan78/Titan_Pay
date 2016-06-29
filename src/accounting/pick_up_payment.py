from src.accounting.payment_method import PaymentMethod

class PickUpPayment(PaymentMethod):
    def __init__(self, full_name, total_pay):
        PaymentMethod.__init__(self)
        self.__full_name = full_name
        self.__total_pay = total_pay

    def pay(self):
        output =  "A check for $" + str(format(self.__total_pay, ',.2f')) + " is waiting for " + self.__full_name + " at the Post Master."
        return output