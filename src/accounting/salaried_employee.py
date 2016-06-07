from src.accounting.employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, salary, commission_rate):
        self.__salary = 0
        self.__commission_rate = 0