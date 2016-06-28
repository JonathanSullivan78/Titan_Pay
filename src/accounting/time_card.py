class TimeCard:
    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def get_timecard_date(self):
        return self.__date

    def calculate_daily_pay(self, rate):
        rate = float(rate)
        end_unit = (int(self.__end_time) // 100) * 60 + (int(self.__end_time) - (int(self.__end_time) // 100) * 100)
        start_unit = (int(self.__start_time) // 100) * 60 + (int(self.__start_time) - (int(self.__start_time) // 100) * 100)
        total_units = end_unit - start_unit

        if total_units > 480:
            standard_time = 480
            overtime_time = total_units - 480

        else:
            standard_time = total_units
            overtime_time = 0

        total_pay = (standard_time / 60) * rate + (overtime_time / 60) * 1.5 * rate

        return total_pay

    def get_date(self):
        return self.__date

    def set_end_time(self, end_time):
        self.__end_time = end_time