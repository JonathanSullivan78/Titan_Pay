class TimeCard:
    def __init__(self):
        self.__date = " "
        self.__start_time = " "
        self.__end_time = " "

    def calculate_daily_pay(self, rate):
        total_hours = self.__end_time - self.__start_time
        if total_hours <= 8:
            daily_pay = total_hours * rate

        else:
            daily_pay = ((1.5 * rate * (total_hours - 8)) + (rate * 8))