from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.direct_deposit_payment import DirectDepositPayment
from src.accounting.mail_payment import MailPayment
from src.accounting.pick_up_payment import PickUpPayment
from tkinter import messagebox


class SalariedEmployee(Employee):

    def __init__(self, employee_id, last_name, first_name, salary, commission_rate, weekly_dues, payment_method, street_address, city, state, zipcode):
        Employee.__init__(self, employee_id, last_name, first_name, weekly_dues, payment_method, street_address, city, state, zipcode)

        self.__salary = float(salary)
        self.__commission_rate = float(commission_rate) / 100
        self.__receipt_list = []

    def make_sale(self, employee_id, last_name, item, units, unit_cost, total):
        receipt = Receipt(employee_id, last_name, item, units, unit_cost, total)
        self.__receipt_list.append(receipt)
        return

    def get_receipt_count(self):
        return len(self.__receipt_list)

    def calculate_pay(self):
        total_pay = 0
        for receipt in self.__receipt_list:
            total_pay += receipt.get_sale() * self.__commission_rate

        total_pay += self.__salary / 12
        weekly_dues = Employee.get_weekly_dues(self)
        total_pay -= float(weekly_dues)

        self.pay(total_pay)

    def pay(self, total_pay):
        full_name = Employee.get_full_name(self)
        if Employee.get_payment_method(self) == 'DD':
            direct_deposit_payment = DirectDepositPayment(full_name, total_pay)
            output = direct_deposit_payment.pay()

        elif Employee.get_payment_method(self) == 'MA':
            full_address = Employee.get_full_address(self)
            mail_payment = MailPayment(full_name, full_address, total_pay)
            output = mail_payment.pay()

        else:
            pick_up_payment = PickUpPayment(full_name, total_pay)
            output = pick_up_payment.pay()

        messagebox.showinfo('Payroll Result', output)

        return(output)