from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.payment_method import PaymentMethod

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method)

        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__payment_method = payment_method
        self.__receipt_list = []

    def make_sale(self, date, sale_amt):
        self.__receipt_list.append(Receipt(date,sale_amt))

    def compute_commission(self):
        commission = self.__commission_rate * self.__receipt_list
        return commission

    def pay(self, salary, commission_rate):
        payment_method = PaymentMethod()
        payment_method.make_payment()

        for rc in self.__receipt_list:
            total_pay = salary + commission_rate
            return total_pay

        return payment_method