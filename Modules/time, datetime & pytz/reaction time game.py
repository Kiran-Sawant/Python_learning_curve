import time
import random

#___________reaction time game____________#
input('Press enter to start')

waitTime = random.randint(1, 5) #selects a random int from 1 to 5 & assigns to var
time.sleep(waitTime) # waits for the time passed in seconds and then executes the further code in the script
startTime = time.time() #records time before input
input('press enter to stop')

endTime = time.time() # records time after input

print("Started at "+ time.strftime('%X', time.localtime(startTime))) 
print("Ended at "+ time.strftime('%X', time.localtime(endTime)))
print("Your reaction time was {} sec".format(endTime - startTime))