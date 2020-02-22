from api_key import mService
from datetime import datetime
from firebase import *
# import sys
text_file = open('test.txt', 'w')


def w(n):
    text_file.write(n)

print("google map direction")

###
# origin = 13.084305, 77.484756
# destination = 13.085230, 77.484800
# dirs  = mService.directions(origin, destination)
#start = 'Orion Mall, Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleshwaram West, Bengaluru, Karnataka 560055'
#end = 'Mantri+Square+Mall,+Sampige+Road,+Malleshwaram+West,+Bengaluru,+Karnataka'

###

origin = Plat, Plong
destination = Dlat, Dlong
now = datetime.now()
directions = mService.directions(origin, destination)  # ,mode='driving', avoid="ferries", departure_time=now)
directions = directions[0]
i = 1
for leg in directions['legs']:
    startAddress = leg['start_address']
    print("Start Address:", startAddress)
    w("Start Address")
    w(startAddress)
    endAddress = leg['end_address']
    w("\nEnd Address")
    w(endAddress)
    print("End Address:", endAddress)
    distance = leg['distance']['text']
    w("Total Distance ")
    w(str(distance))
    print("Distance:", distance)
    duration = leg['duration']['text']
    w("\n Total Time ")
    w(str(duration))
    print("Duration:", duration)
    for step in leg['steps']:
        html_instructions = step['html_instructions']
        print("STEP: {} {}".format(i, html_instructions))
        w("\n")
        w(str(html_instructions))
        w("<b> on same road </b>\n")
        i = i + 1
        lDistance = step['distance']['value']
        lTime = step['duration']['text']
        w(str(lDistance))
        print("Distance", lDistance, "Time", lTime)


text_file.close()
"""
Write o/p console screen text file from function
orig = sys.stdout
with open("output.py", "w+") as f:
    sys.stdout = f
    try:
        execfile("test.py", {})
    finally:
        sys.stdout = orig
"""