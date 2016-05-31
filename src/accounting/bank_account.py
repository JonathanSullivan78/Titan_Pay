class BankAccount:
    def __init__(self):
        self.__bank_name = " "
        self.__routing_number = " "
        self.account_id = " "

    def deposit(self, amt):
        print("Depositing $" + amt + "in " + self.__bank_name + " using Routing Number: " + self.__routing_number)