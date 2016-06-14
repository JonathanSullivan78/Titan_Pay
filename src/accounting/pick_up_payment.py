from src.accounting.payment_method import PaymentMethod


class MailPayment(PaymentMethod):
    def __init__(self, first_name, last_name, total_pay):
        PaymentMethod.__init__(self, first_name, last_name, total_pay)

    def pay(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission):
        return "A check for $" + total_pay+ "is waiting for " + first_name + " " + last_name + " at the PostMaster."