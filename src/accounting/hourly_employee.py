from src.accounting.employee import Employee

class Hourly_Employee(Employee):
    def __init__(self, hourly_rate):
        self.__hourly_rate = 0