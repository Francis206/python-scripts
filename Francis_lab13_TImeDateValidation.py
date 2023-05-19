# IT 280 – Lab #13: Time and Date Instructions by Francis @ 2022

import datetime


def askTime(text):
    while True:
        try:
            print('Please, a date in YYYY-MM-DD format', text, end=': ')
            date = input()
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print('ERROR - Date must be informed in a proper format "YYYY-MM-DD"')

    print("This is the date: ",  date.strftime('%B %d, %Y'))
    return date


def printTimeStamp1(start, end):
    duration = end - start
    years = divmod(duration.total_seconds(), 31518720)
    months = divmod(years[1], 2626560)
    days = divmod(months[1], 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = divmod(minutes[1], 1)
    print("Time between this event to now is:  %d years, %d months, %d days, %d hours, %d minutes and  %d seconds." % (years[0], months[0], days[0], hours[0], minutes[0], seconds[0]))

def printTimeStamp2(start):
    duration = start
    years = divmod(duration.total_seconds(), 31518720)
    months = divmod(years[1], 2626560)
    days = divmod(months[1], 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = divmod(minutes[1], 1)
    print("Time between this event to previous event is:   %d years, %d months, %d days, %d hours, %d minutes and  %d seconds." % (years[0], months[0], days[0], hours[0], minutes[0], seconds[0]))

def main():
    napoleao = askTime('The birthdate of Napoleon Bonaparte')
    printTimeStamp1(napoleao, datetime.datetime.now())

    pearHarbor = askTime('The bombing of Pearl Harbor')
    different = pearHarbor - napoleao
    printTimeStamp1(pearHarbor, datetime.datetime.now())
    printTimeStamp2(different)

    wrightBrothers = askTime('The Wright Brothers 1st flight')
    different2 = pearHarbor - wrightBrothers
    printTimeStamp1(wrightBrothers, datetime.datetime.now())
    printTimeStamp2(different2)


main()
