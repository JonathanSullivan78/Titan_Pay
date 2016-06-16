class Receipt:
    def __init__(self, date, sale_amount):
        self.__date = date
        self.__sale_amount = sale_amount

    def get_sale(self):
        return self.__sale_amount