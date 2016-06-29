from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard
from src.accounting.direct_deposit_payment import DirectDepositPayment
from src.accounting.mail_payment import MailPayment
from src.accounting.pick_up_payment import PickUpPayment


class HourlyEmployee(Employee):
    def __init__(self, employee_id, last_name, first_name, hourly_rate, weekly_dues, payment_method, street_address, city, state, zipcode):
        Employee.__init__(self, employee_id, last_name, first_name, weekly_dues, payment_method, street_address, city, state, zipcode)
        self.__hourly_rate = hourly_rate
        self.__time_cards = []

    def clock_in(self, date, start_time):
        end_time = ""
        timecard = TimeCard(date, start_time, end_time)
        self.__time_cards.append(timecard)

    def clock_out(self, date, end_time):
        for t in self.__time_cards:
            if t.get_date() == date:
                t.set_end_time(end_time)

    def calculate_pay(self):
        total_pay = 0
        for time_card in self.__time_cards:
            total_pay += time_card.calculate_daily_pay(self.__hourly_rate)

        if total_pay > 0:
            weekly_dues = float(Employee.get_weekly_dues(self))
            total_pay -= weekly_dues
            self.total_payment(total_pay)

    def total_payment(self, total_pay):
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

        print(output)

