class Employee:
    def __init__(self, employee_id, first_name, last_name, weekly_dues):
        self.__employee_id = 0
        self.__first_name = " "
        self.__last_name = " "
        self.__weekly_dues = 0

    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name