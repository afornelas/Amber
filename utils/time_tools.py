import time

def current_hour():
    """Hour (12-hour clock) as a integer [01,12]"""
    return int(time.strftime("%I"))

def current_weekday():
    """Weekday as a decimal number [0(Sunday),6]"""
    return int(time.strftime("%w"))

def to_hour(seconds):
    """Converts seconds since unix Epoch into an easy to 
    read version, for example, 1649211262 becomes 07:14 PM"""
    return time.strftime("%I:%M %p",time.localtime(seconds))

def to_day(seconds):
    """Converts seconds since unix Epoch into an easy to 
    read version, for example, 1649211262 becomes Tuesday"""
    return time.strftime("%A",time.localtime(seconds))

    '''double check functions for time zones!'''