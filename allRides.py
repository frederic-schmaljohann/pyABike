#!/usr/bin/python
from PyABike import *

cab = PyABike()

userName='' # either Kundennummer or telephone number
password=''

rides = []
newRides = []
i = 0
while (i == 0 or (len(newRides) != 0)):
    newRides = cab.listCompletedTrips(i*20, 20, '','',userName, password)[1]
    if (len(newRides) != 0):
        rides += newRides[0]
        print '{} rides collected'.format(len(rides))
    i = i + 1

ridesStr = ""
for r in rides:
    ridesStr += str(r["StartTime"]) + "," + str(r["EndTime"]) + "," + r["BikeNumber"] + "\n"

f= open('sample_rides.csv', 'w')
f.write(ridesStr)
f.close()
