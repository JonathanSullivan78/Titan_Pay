from src.accounting.address import Address

class Employee:
    def __init__(self, employee_id, last_name, first_name, weekly_dues, payment_method, street_address, city, state, zip_code):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        self.__payment_method = payment_method
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__full_address = street_address + "- " + city + ", " + state + "  " + zip_code

    def get_full_name(self):
        full_name = self.__first_name + " " + self.__last_name
        return full_name

    def get_weekly_dues(self):
        return self.__weekly_dues

    def get_payment_method(self):
        return self.__payment_method

    def get_full_address(self):
        return self.__full_address