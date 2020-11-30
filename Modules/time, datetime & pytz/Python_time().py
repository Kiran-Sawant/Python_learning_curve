import time

UTCtime = time.gmtime() # gives UTC time(London time) as a time.struct
print(UTCtime)

localTime = time.localtime() #gives local time
print(localTime)

time.time() #gives time since epoch in seconds

time.sleep(2) #takes number of sec as param & stops the program for that no of sec

k = time.perf_counter() #gives time taken since process start to this line including sleep
print(k)

j = time.process_time() #gives time taken by the CPU to process the code upto this line excluding sleep
print(j)

print(time.strftime('%A %d %m %Y', localTime)) #strftime takes a time.struct & gives the dates and time in
                                               #a desired format as a string, format is given by the flags passed in args

strp = time.strptime("12 Feb 20", '%d %b %y') #Inverse of .strftime, retrns a time.struct from string
print(strp)

info = time.get_clock_info('process_time') #gives information about a perticular type of clock
print(info)

#.tzname gives the system timezone name & .timezone gives the offset from UTC
print("The timezone on the system is {0} with an offset of {1}".format(time.tzname, time.timezone))

if time.daylight != 0: #.daylight passes a boolean for localtime
    print("\tDaylight savings is in effect")