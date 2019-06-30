import random
import time

#Convert a 10-digit timestamp to a time string, defaulted to the "%Y-%m-%d %H:%M:%S" format
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


#Converts a time string to a 10-digit timestamp, which defaults to the "%Y-%m-%d %H:%M:%S" format
def date_to_timestamp(date, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.strptime(date, format_string)
    time_stamp = int(time.mktime(time_array))
    return time_stamp

#Get a random time in range
def get_random_date(start_date='2019-01-26 10:00:00',end_date='2019-01-26 23:00:00'):
    start_time = date_to_timestamp(start_date)
    end_time = date_to_timestamp(end_date)

    interval_seconds = start_time-end_time

    v = random.randint(0,255)+random.randint(0,255)*2**8+random.randint(0,255)*2**16+random.randint(0,127)*2**24
    v = v/2147483647

    interval_seconds = int(-interval_seconds*v)
    final_time = timestamp_to_date(start_time+interval_seconds)

    return final_time


if __name__ == "__main__":
    print(get_random_date(start_date='2019-01-26 11:44:17',end_date='2019-01-26 22:57:34'))