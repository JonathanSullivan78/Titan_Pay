import datetime
from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard


class Hourly_Employee(Employee):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)

        self.__hourly_rate = hourly_rate
        self.__time_card = []

    def clock_in(self):
        start_time = datetime.datetime.now()
        self.__time_card.append(start_time)

    def clock_out(self, date, end_time):
        end_time = datetime.datetime.now()
        self.__time_card.append(end_time)

    def pay(self, timecard, ):
        #Got Lost Here - Headed to LSC w/ Your Other Feedback to Implement Pay - and fix all other issues
