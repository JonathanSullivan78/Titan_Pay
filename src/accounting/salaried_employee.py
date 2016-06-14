from src.accounting.employee import Employee
from src.accounting.receipt import Receipt

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)

        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipt_list = []

    def make_sale(self, date, sale_amt):

        self.__receipt_list.append(Receipt(date,sale_amt))

    def pay(self, salary, commission_rate):
        total_pay = 0
        #Got Lost Here - Headed to LSC w/ Your Other Feedback to Implement Pay - and fix all other issues