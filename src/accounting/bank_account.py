class BankAccount:
    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name
        self.__routing_number = routing_number
        self.__account_id = account_id

    def deposit(self, full_name, amount):
        self.__amount = float(amount)
        self.__full_name = full_name
        output = "I'm depositing $" + str(format(self.__amount, ',.2f')) + " in " + self.__bank_name + " Account Number: " \
                 + self.__account_id + " using Routing Number: " + self.__routing_number + " for " + self.__full_name
        return output
