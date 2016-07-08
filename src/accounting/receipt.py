class Receipt:
    def __init__(self, employee_id, last_name, item, units, unit_cost, total_amount):
        self.__employee_id = employee_id
        self.__last_name = last_name
        self.__item = item
        self.__units = units
        self.__unit_cost = unit_cost
        self.__total_amount = total_amount

    def get_sale(self):
        total = self.__units * self.__unit_cost
        return total
