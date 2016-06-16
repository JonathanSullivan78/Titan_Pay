class TimeCard:
    def __init__(self, start_time, end_time):
        self.__date = " "
        self.__start_time = "0:00"
        self.__end_time = "0:00"

    def calculate_daily_pay(self, rate):
        import datetime as dt
        start_date = dt.datetime.strptime(self.__start_time, '%H:%M')
        end_date = dt.datetime.strptime(self.__end_time, '%H:%M')
        diff = (end_date - start_date)
        total_hours = diff.seconds/60/60
        if total_hours <= 8:
            daily_pay = total_hours * rate

        else:
            daily_pay = ((1.5 * rate * (total_hours - 8)) + (rate * 8))

        return daily_pay
