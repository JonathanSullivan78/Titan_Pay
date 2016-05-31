class SalariedEmployee:
    def __init__(self):
        self.__employee_id = 0
        self.__first_name = " "
        self.__last_name = " "
        self.__salary = 0
        self.__commission_rate = 0
        self.__weekly_dues = 0

    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name