class Clock:

    def __init__(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=1):
        self._days = days
        self._days += (360 * years)
        self._days += (30 * months)
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        return f"<days={self.days} hours={self.hours} minutes={self.minutes} seconds={self.seconds} {self.__class__.__module__}.{self.__class__.__name__}>"

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        self._days = value

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._minutes = value

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        self._seconds = value

    def format(self):
        years = 0; years_format = ""
        months = 0; months_format = ""
        days = self.days; days_format = ""
        hours = self.hours
        minutes = self.minutes
        seconds = self.seconds

        if seconds >= 60:
            minutes += (seconds // 60)
            seconds = (seconds % 60)
        if minutes >= 60:
            hours += (minutes // 60)
            minutes = (minutes % 60)
        if hours >= 24:
            days += (hours // 24)
            hours = (hours % 24)

        seconds_format = f'{seconds}s'
        minutes_format = f'{minutes}m{" " if seconds != 0 else ""}'
        hours_format = f'{hours}h '

        if days >= 30:
            months = days // 30
            months_format = f"{months}m "
            if months >= 12:
                years = months // 12
                months = months % 12
                years_format = f"{years}y "
                months_format = f"{months}m "
            days = days % 30
            days_format = f"{days}d "
        else:
            days_format = f"{days}d "

        if years+months+days == 0:
            days_format = ""
        if years+months+days+hours == 0:
            hours_format = ""
        if seconds == 0:
            seconds_format = ""

        return f"{years_format}{months_format}{days_format}{hours_format}{minutes_format}{seconds_format}"

    def fromFormat(self, timeFormat):
        time = timeFormat.split(' ')
        if time[-1][-1] != 's':
            time.insert(len(time), '0s')
        time_ = time.copy()
        for e, i in enumerate(time_):
            time[e] = ''.join(list(filter(lambda k: k.isdigit(), i)))
        time = list(map(int, time))

        if len(time) < 6:
            for i in range(6-len(time)):
                time.insert(0, 0)

        return Clock(**dict(zip(['years', 'months', 'days', 'hours', 'minutes', 'seconds'], time)))

    def fromSeconds(self, seconds):
        days = (seconds // 86400)
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)
        return Clock(0, 0, days, hours, minutes, seconds)

    def inSeconds(self):
        SECONDS_IN_MINUTE = 60
        SECONDS_IN_HOUR = 3600
        SECONDS_IN_DAY = 86400

        return (self.minutes * SECONDS_IN_MINUTE) + (self.hours * SECONDS_IN_HOUR) + (self.days * SECONDS_IN_DAY) + (self.seconds)