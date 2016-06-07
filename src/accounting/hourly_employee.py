from src.accounting.employee import Employee

class Hourly_Employee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__hourly_rate = 0