from src.accounting.payment_method import PaymentMethod
from src.accounting.bank_account import BankAccount

class DirectDepositPayment(PaymentMethod):
    def __init__(self, full_name, total_pay):
        PaymentMethod.__init__(self)
        self.__full_name = full_name
        self.__total_pay = total_pay

    def pay(self):
        bankaccount = BankAccount('Bank Name', 'Routing Number', 'Account Number')
        output = bankaccount.deposit(self.__full_name, self.__total_pay)
        return output