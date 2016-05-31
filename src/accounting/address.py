class Address:
    def __init__(self, street_address, city, state, zip):
        self.__street_address = " "
        self.__city = " "
        self.__state = " "
        self.__zip = " "

    def get_address(self):
        return self.__street_address + ' ' + self.__city + ', ' + self.__state + '. ' + self.__zip