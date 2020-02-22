import googlemaps
from multiprocessing import Process
from EngineDirection import EngineDirection as En_Dir
from Engine import *

"""
file open for reading direction and storing single value in list
"""
lines = []
with open('test.txt') as fo:
    for record in fo:
        # print(record.split('<b>')[0])
        lines.append(record)  # store the all text file in list naming lines
target = len(lines)
# print("target no. of result",target)
dir_cmd = []  # list initialize for storing the split of all final cmd of direction
for i in range(2, target, 2):
    result = lines[i]
    result = result.replace('</b>', '<b>')
    dir_cmd.append(result.split('<b>'))  # append the all result value in list dir_line
    # print(l[0])


"""
same txt file open for reading distance b/w two direction cmd and storing single-single value in list
"""
global distance_index # it initialize the index value of distance
distance_index = 0
distance_lines = []  # store the all result of distance in distance_lines list
with open('test.txt') as fo:
    for record in fo:
        # print(record.split('<b>')[0])
        distance_lines.append(record)
target = len(distance_lines)
distance_result = []  # initialize the distance_result for store the single value
for i in range(3, target, 2):
    result = distance_lines[i]
    # print(result)
    distance_result.append(result)

len_of_l = len(dir_cmd)
# print(len_of_l)
# print(l[18][0])
dir_cmd_fList = []
dir_cmd_sList = []


def main_list():
    for m in range(len_of_l):
        for n in range(1):
            dir_cmd_fList.append(dir_cmd[m][0])
             # print(l[m][0])


def sub_list():
    for m in range(len_of_l):
        for n in range(1):
            dir_cmd_sList.append(dir_cmd[m][1])
            # print(l[m][1])


main_list()
sub_list()

# variable declare
turns = "Turn"
heads = "Head"
slights = "Slight"
keeps = "Keep"
makes = "Make a"
atRoundAbouts = "At the roundabout, take the"
continuess = "Continue onto"
continue_straights = "Continue straight"

# set declare
turn = set(turns.split())
head = set(heads.split())
slight = set(slights.split())
keep = set(keeps.split())
make = set(makes.split())
continues = set(continuess.split())
atRoundAbout = set(atRoundAbouts.split())
continue_straight = set(continue_straights.split())

# sub-variable declare
souths = "south"
norths = "north"
easts = "east"
wests = "west"
northeasts = "northeast"
northwests = "northwest"
southeasts = "southeast"
southwests = "southwest"
lefts = "left"
u_turns = "U-turn"
exitss = "exit onto"
rights = "right"
sharps = "Sharp"

# sub-set declare
sharp = set(sharps.split())
northeast = set(northeasts.split())
northwest = set(northwests.split())
southeast = set(southeasts.split())
southwest = set(southwests.split())
south = set(souths.split())
north = set(norths.split())
east = set(easts.split())
west = set(wests.split())
right = set(rights.split())
left = set(lefts.split())
u_turn = set(u_turns.split())
exits = set(exitss.split())


def main_function_start():
    global distance_index
    for a in range(len_of_l):
        # print(fList[a])
        set1 = set(dir_cmd_fList[a].split())
        set2 = set(dir_cmd_sList[a].split())
        if set1 == turn and set2 == left:
            print("turn left main cmd")
            turn_left()
        elif set1 == turn and set2 == right:
            print("turn right main cmd")
            turn_right()
        elif set1 == head and set2 == south:
            print("head south main cmd")
            En_Dir.head_south()
        elif set1 == head and set2 == north:
            print("head north main cmd")
            En_Dir.head_north()
            forward_measured_distance()
            distance_index += 1
        elif set1 == head and set2 == east:
            print("head east main cmd")
            En_Dir.head_east()
        elif set1 == head and set2 == west:
            print("head west main cmd")
            En_Dir.head_west()
        elif set1 == head and set2 == northeast:
            print("head northeast main cmd")
            En_Dir.head_northEast()
            forward_measured_distance()
            distance_index += 1
        elif set1 == head and set2 == northwest:
            print("head northwest main cmd")
            En_Dir.head_northWest()
        elif set1 == head and set2 == southeast:
            print("head southeast main cmd")
            En_Dir.head_southEast()
        elif set1 == head and set2 == southwest:
            print("head southwest main cmd")
            En_Dir.head_southWest()
        elif set1 == keep and set2 == left:
            print("keep left main cmd")
            keep_left()
        elif set1 == keep and set2 == right:
            print("keep right main cmd")
            keep_right()
        elif set1 == slight and set2 == left:
            print("slight left main cmd")
            slight_left()
        elif set1 == slight and set2 == right:
            print("slight right main cmd")
            slight_right()
        elif set1 == make and set2 == u_turn:
            print("Make a u-turn main cmd")
            make_u_turn()
        elif set1 == continues:
            print("continue on to main cmd")
            continues_onto()
        elif set1 == continue_straight:
            print("continue straight main cmd")
            continue_straight()
        elif set1 == atRoundAbout and set2 == exits:
            print("at roundAbout take specify exit main cmd")
            atRoundabout()
        elif set1 == sharp and set2 == right:
            print("sharp right main cmd")
            sharpRight()
        elif set1 == sharp and set2 == left:
            print("sharp left main cmd")
            sharpLeft()
        else:
            print("             **** No matched **** so going straight if.....else main cmd")
            continue_straight()
def right():
    print("right function")


def left_func():
    print("left function")
    right()


def forward_measured_distance():
    global current_distance
    print("measured distance")
    En_Dir.defaultLocation()
    distance_cmd = int(distance_result[distance_index])
    while distance_cmd > En_Dir.currentRotation():
        left_func()


def start():
    ###
    # fetch the user cuurent booking throught the raspberry pu and
    # android app and same update to the firebase then main start python file
    # after detect it and let the mapfunction ready the path for pickup and destination
    ###
    En_Dir.currentRotation()
    main_function_start()


start()

