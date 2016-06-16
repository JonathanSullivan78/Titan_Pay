from src.accounting.payment_method import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay):
        PaymentMethod.__init__(self, first_name, last_name)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__total_pay = total_pay

    def pay(self, first_name, last_name, street_address, city, state, zip_code, total_pay):
        return "Mailing a check to " + first_name + " " + last_name + " for $" + total_pay + " to " + street_address + " " + city + ", " + state + " " + zip_code