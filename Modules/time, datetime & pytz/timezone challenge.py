import datetime as dt
import pytz

zoneMenu = {'London':'Europe/London',
            'Tokyo':'Asia/Tokyo',
            'New York':'America/New_York',
            'Sydney':'Australia/Sydney',
            'Dubai':'Asia/Dubai',
            'Zurich':'Europe/Zurich',
            'Berlin':'Europe/Berlin',
            'Hong Kong':'Asia/Hong_Kong',
            'Jerusalem':'Asia/Jerusalem'}

condition = True
while condition:
    for city in zoneMenu:
        print(city, end=', ')
    choice = input("\nselect any one of the above cities or 0 to quit: ")
    if choice == '0':
        condition = False
        continue
    timeZone = pytz.timezone(zoneMenu[choice])

    zoneTime = dt.datetime.now().astimezone(timeZone)
    localTime = dt.datetime.now().astimezone()
    utcTime = dt.datetime.utcnow().astimezone(pytz.timezone('UTC'))

    # print(zoneTime, '', zoneTime.tzinfo)
    # print(localTime, '', localTime.tzinfo)
    # print(utcTime, '', utcTime.tzinfo, '\n')

    print("The current date in {0} is {1} & time is {2}".format(choice, zoneTime.date(), zoneTime.time()), zoneTime.tzinfo)
    print("your current date is {0} & time is {1}".format(localTime.date(), localTime.time()), localTime.tzinfo)
    print("current UTC date is {0} & time is {1}".format(utcTime.date(), utcTime.time()), utcTime.tzinfo,'\n')
else:
    print("Fuck off!!")