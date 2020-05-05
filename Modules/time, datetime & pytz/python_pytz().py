import pytz
import datetime

#_________creating a pytz() timezone object________#
country = 'Europe/Moscow' #creating a string to pass in .timezone()
tZone = pytz.timezone(country) #creating a timezone object
localTime = datetime.datetime.now(tZone) #getting the local time of the timezon passed in .now()

print("The time in {0} is {1}".format(country, localTime))
print("UTC is {}\n".format(datetime.datetime.utcnow()))

#________Retriving valid .timezone() strings________#

# for i in pytz.all_timezones: #.all_timezones is a list of valid pytz timezone strings
#     print(i)

# for x in sorted(pytz.country_names): #.countrynames is a dict of valid country names
#     print(x, pytz.country_names[x])

# for x in sorted(pytz.country_names): 
#     print('{0}:{1}'.format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones: #.country_timezones is a dict() of timezones inside of countries
#         for zone in sorted(pytz.country_timezones[x]):
#             tZone2 = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tZone2)
#             print('{0}:{1}'.format(zone, local_time))
#     else: print('\t\t no time zone available')

#_______aware & unaware datetime()________#

local_Time =datetime.datetime.now()
UTCtime =datetime.datetime.utcnow()

print("Naive local time is {}".format(local_Time))
print("Naive UTC time is {}".format(UTCtime))

awareUTCtime = pytz.utc.localize(UTCtime) #localize() is used to convert an unaware datetime() to an aware
                                          #datetime()
awareLocalTime = pytz.utc.localize(UTCtime).astimezone() # .astimezone() takes timezone object & gives an aware
                                                         #datetime object for that timezone w.r.t the passed
                                                         #datetime object in .utc.localize() *default machine timezone

print("\nAware Local Time is {}, timezone is {}".format(awareLocalTime, awareLocalTime.tzinfo))
print("Aware UTC Time is {}, timezone is {}".format(awareUTCtime, awareUTCtime.tzinfo))

#____________________Adjustment for daylight savings_____________________#

gapTime = datetime.datetime(2019, 10, 25, 1, 30, 0, 0)
print(gapTime)
print(gapTime.timestamp())

s = 1571967000
t = s + (60 * 60)

gb = pytz.timezone("UTC")
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print('{} seconds since the epoch is {}'.format(s, dt1))
print('{} seconds since the epoch is {}'.format(t, dt2))