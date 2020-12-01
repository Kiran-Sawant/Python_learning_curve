import datetime
import pytz
import time

# Creating a timezone object
Tzone = pytz.timezone('America/New_York')

#________________________________datetime creating methods_______________________________________#
# .today() gives the local date & local time of the system
LocalTime = datetime.datetime.today()
print('System Local time is: ', LocalTime)

# .now() gives local time, .astimezone() takes a timezone element for .now() method
#that gives local time of the timezone passed
InternationalTime = datetime.datetime.now().astimezone(Tzone)
print('NewYork time is: ', InternationalTime)

# .tcnow() gives the current UTC date & time
utc = datetime.datetime.utcnow()
print('UTC time is: ', utc)

# .fromtimestamp() gives a datetime object from passed POSIX time stamp
Time = datetime.datetime.fromtimestamp(time.time())
print('Time from timestamp: ', Time)

# .combine() creates a new datetime from the passed date, time & tzelement
combo = datetime.datetime.combine(LocalTime.date(), utc.time(), InternationalTime.tzinfo)
print('local date with UTC time & NY timezone: ', combo)

#___________________________.datetime() attributes___________________________________#
print('\n\nPrecision: ', LocalTime.resolution)#returns te precision of datetime
print('Year: ', LocalTime.year)               #returns the year of datetime object
print('month: ', LocalTime.month)             #returns the month of datetime
print('day: ', LocalTime.day)                 #returns the day of the month of datetime
print('Weekday: ', LocalTime.weekday())       #returns the weekday of the date as monday being 0 & sunday 6
print('hour: ', LocalTime.hour)               #returns the hour of datetime
print('minute: ', LocalTime.minute)           #returns the minute of datetime
print('Second: ', LocalTime.second)           #returns the seconds of datetime
print('tzinfo: ', LocalTime.tzinfo)           #returns the tzinfo of datetime
print('DST in NY: ', InternationalTime.fold, '\n') #1 if DST & 0 if not DST

print('Date: ', LocalTime.date())             #returns the entire date of datetime
print('Time: ', LocalTime.time())             #returns the entire time of datetime
print(LocalTime.timetuple())                  #returns time.struct() of the datetime
print('timestmp: ', LocalTime.timestamp())    #returns the timestamp of datetime
print('NY time is:', InternationalTime.strftime('%dth %b %Y %I:%M %p - %Z')) #passing string according to time.strftime() directives

#____________________Adjustment for daylight savings_____________________#

# gapTime = datetime.datetime(2019, 10, 25, 1, 30, 0, 0)
# print(gapTime)
# print(gapTime.timestamp()) #.timestamp() gives the POSIX time of applied datetime()

# s = 1571967000
# t = s + (60 * 60)

# gb = pytz.timezone("UTC")
# dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb) # gives aware datetime object from
# dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb) #passed timestamp in .timestamp()

# print('{} seconds since the epoch is {}'.format(s, dt1))
# print('{} seconds since the epoch is {}'.format(t, dt2))