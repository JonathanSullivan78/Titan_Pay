from src.accounting.payment_method import PaymentMethod
from src.accounting.bank_account import BankAccount

class DirectDepositPayment(PaymentMethod):
    def __init__(self, total_pay, bank_name, routing_number, account_id):
        PaymentMethod.__init__(self, total_pay, bank_name, routing_number, account_id)

    def pay(self, total_pay, bank_name, routing_number, account_id):
        return "Depositing $" + total_pay+ "in " + bank_name + " Account Number: " + account_id + " using Routing Number: " + routing_number