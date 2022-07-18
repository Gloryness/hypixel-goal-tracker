import os

__title__ = 'app'
__author__ = 'Gloryness'
__license__ = 'MIT License'
__version__ = '1.0.0'
__module__ = os.getcwd()

if not __module__.endswith("app"):
    __module__ = __module__+'\\'
    is_executable = True
else:
    __module__ = __module__.replace("/", "\\").replace("src\\app", "")
    is_executable = False

path = lambda *p: __module__+'\\'.join(p)

def convert_to_time(x):
    """
    Convert x to a time format (Only goes up to 24 hours)
    23 --> 00:23
    103 --> 01:43
    3610 --> 01:00:10
    86400 --> 24:00:00
    86460 --> 24:01:00 (As you can see, it wont go up to days but still works properly)
    :return: str
    """
    minute = 60
    MINUTE_STEPS = [i for i in range(60, 60 * 32000, 60)]
    MINUTE_STEPS2 = tuple(MINUTE_STEPS.copy()) # Turning this into a tuple since we dont want it to be changed, only read.
    HOUR_STEPS = [i for i in range(3600, 3600 * 32000, 3600)]
    if x < minute:
        return f'00:{"0" if len(str(x)) == 1 else ""}{x}'
    elif x >= minute:
        for minute_ in MINUTE_STEPS:
            if x >= minute_ and x < MINUTE_STEPS[MINUTE_STEPS.index(minute_+60)]:
                def _calculate_second_pos(x):
                    upcoming_minute = MINUTE_STEPS[MINUTE_STEPS.index(minute_+60)] # Find the upcoming minute, then see how much apart we are from it.
                    dist = abs(abs(x-upcoming_minute)-60) # Finding the inbetween of x-y with abs()
                    return f'{"0" if len(str(dist)) == 1 else ""}{dist}'
                def _calculate_minute_pos(x):
                    end = MINUTE_STEPS.index(minute_)+1
                    for index, min_ in enumerate(MINUTE_STEPS2, start=1):
                        if end >= min_ and end < min_+60:
                            # If index is 60, then remove all way up to 3600 (60*60) in MINUTE_STEPS therefore the 60 will turn into 0
                            for a in range(60, MINUTE_STEPS[MINUTE_STEPS.index(3600)]*index+1, 60): MINUTE_STEPS.remove(a)
                            calculate_end = MINUTE_STEPS.index(minute_+60)
                            break
                        elif end < 60:
                            calculate_end = end # If we're below 3600 (60) which is an hour, then its safe to give the 'end' value, which in this case is 60.
                            break
                    return f'{"0" if calculate_end < 10 or MINUTE_STEPS.index(minute_)+1 < 10 else ""}{calculate_end}'
                def _calculate_hour_pos(x):
                    for hour_ in HOUR_STEPS:
                        if x < 3600: # Dont need any hour if below 3600
                            return ''
                        if x >= hour_ and x < HOUR_STEPS[HOUR_STEPS.index(hour_+3600)]: # Calculating the index of hour_ in HOUR_STEPS if 'x' is >= than hour_
                            return f'{"0" if HOUR_STEPS.index(hour_)+1 < 10 else ""}{HOUR_STEPS.index(hour_)+1}:'

                return f'{_calculate_hour_pos(x)}{_calculate_minute_pos(x)}:{_calculate_second_pos(x)}'