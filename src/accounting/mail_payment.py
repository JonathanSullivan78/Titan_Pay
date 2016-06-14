from src.accounting.payment_method import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay):
        PaymentMethod.__init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay)

    def pay(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission):
        return "Mailing a check to " + first_name + " " + last_name + " for $" + total_pay + " to " + street_address + " " + city + ", " + state + " " + zip_code

