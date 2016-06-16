from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard
from src.accounting.payment_method import PaymentMethod


class Hourly_Employee(Employee):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method)
        self.__hourly_rate = hourly_rate
        self.__payment_method = payment_method
        self.__time_cards = []

    def clock_in(self, date, start_time):
        time_card = TimeCard()
        time_card.set_date(date)
        time_card.set_time(start_time)
        self.__time_cards.append(time_card)

    def clock_out(self, date, end_time):
        time_card = TimeCard()
        time_card.get_date(date)
        time_card.set_time(end_time)
        for tc in self.__time_cards:
            if time_card.get_date == time_card.set_date:
                time_card.set_end_time()

    def pay(self, date, rate):
        payment_method = PaymentMethod()
        payment_method.make_payment()
        for tc in self.__time_cards:
            time_card = TimeCard(date)
            time_card.calculate_daily_pay(rate)
            total_pay = 0
            total_pay += time_card.calculate_daily_pay()
            return total_pay
        return payment_method