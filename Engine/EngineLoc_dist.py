import pyrebase
# in this page engine default current location getting , current comapss Rotation value getting

# firebase config
config = {
  "apiKey": "AIzaSyAY6J15m0dP9NUHElJlNogCJ56iCT-cWrM",
  "authDomain": "compassmodule-35cfe.firebaseapp.com",
  "databaseURL": "https://compassmodule-35cfe.firebaseio.com",
  "storageBucket": "compassmodule-35cfe.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


# default location
def defaultLocation():
    print("")
    defaultLocDb = db.child("EngineLocation").get()
    totalItems = dict(defaultLocDb.val())
    print(totalItems.values())
    Defaullat = totalItems["latitude"]
    Defaultlong = totalItems["longitude"]
    print("latitude = {} \nlongtitude = {}".format(Defaullat, Defaultlong))


# current location
def currentLocation():
    print("")
    currentLocDb = db.child("CurrentRider").child("Destination").get()


def currentRotation():
    global degree
    rotation = db.child("CurrentRotation").get().val()
    degree = int(rotation)
    print("rotate =", degree)


def turn_left():
    print("turn left function")


def rotate_steering_left(l_deg):
    while degree <= l_deg:
        currentRotation()
        turn_left()


def turn_right():
    print("turn right function")


def rotate_steering_right(r_deg):
    while degree <= r_deg:
        currentRotation()
        print("turning right ")



def shift_default_direction():
    if degree == 0 or degree == 45 or degree == 90 or degree == 135 or degree == 180 or degree == 225 \
            or degree == 270 or degree == 315 or degree == 360:
        print("no need to change set True")
    elif 22 >= degree >= 0:
        currentRotation()
        while degree <= 90:
            currentRotation()
            turn_left()    # to set the engine direction at 0• direction(north)
        print("about to north 22")
    elif 22 < degree < 45:
        rotate_steering_right(45)  # to set the engine direction at 45* direction(North-East)
        print("about to North east < 22")
    elif 45 < degree < 67:
        rotate_steering_left(45)
        print("about to North east 67")
    elif 67 <= degree < 90:
        rotate_steering_right(90)
        print("about to North east < 67")
    elif 90 < degree < 112:
        rotate_steering_left(90)
        print("about to North east 112")
    elif 112 <= degree < 135:
        rotate_steering_right(135)
        print("about to North east <112")
    elif 135 < degree < 157:
        rotate_steering_left(135)
        print("about to North east 157")
    elif 157 <= degree < 180:
        rotate_steering_right(180)
        print("about to North east< 157")
    elif 180 < degree < 202:
        rotate_steering_left(180)
        print("about to North east 202")
    elif 202 <= degree < 225:
        rotate_steering_right(225)
        print("about to North east <202")
    elif 225 < degree < 247:
        rotate_steering_left(225)
        print("about to North east 247")
    elif 247 <= degree < 270:
        rotate_steering_right(270)
        print("about to North east <247")
    elif 270 < degree < 292:
        rotate_steering_left(270)
        print("about to North east 292")
    elif 292 <= degree < 315:
        rotate_steering_right(315)
        print("about to North east <292")
    elif 315 < degree < 337:
        rotate_steering_left(315)
        print("about to North east 337")
    elif 337 <= degree < 360:
        rotate_steering_right(0)
        print("about to North east <337")
    else:
        print("no matched direction degree")


def head_south():
    print("head south function")
    if 175 <= degree <= 185:
        print("all ready in head south direction")
    elif 0 <= degree < 180:
        print("from north or east to south")
        currentRotation()
        while degree < 180:
            currentRotation()
            turn_right()
    elif 190 <= degree <= 350:
        print("from north or west to head south")
        currentRotation()
        while degree > 180:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_north():
    print("head north function")
    if 355 <= degree <= 5:
        print("all ready in head north direction")
    elif 180 <= degree < 355:
        print("from north or east to south")
        currentRotation()
        while degree < 355:
            currentRotation()
            turn_right()
    elif 5 <= degree <= 180:
        print("from north or west to head south")
        currentRotation()
        while degree > 5:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_east():
    print("head east function")
    if 85 <= degree <= 95:
        print("all ready in head east direction")
    elif 0 <= degree <= 85:
        print("from north or east to south")
        currentRotation()
        while degree < 85:
            currentRotation()
            turn_right()
    elif 360 >= degree >= 95:
        print("from north or west to head south")
        currentRotation()
        while degree > 95:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_west():
    print("head west function")
    if 265 <= degree <= 275:
        print("all ready in head west direction")
    elif 90 <= degree <= 265:
        print("from north or east to south")
        currentRotation()
        while degree < 265:
            currentRotation()
            turn_right()
    elif 275 <= degree <= 360 or 0 <= degree >= 90:
        print("from north or west to head south")
        currentRotation()
        while degree <= 90 or degree >= 275:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_northEast():
    print("head northeast function")
    if 40 <= degree <= 50:
        print("all ready in head south direction")
    elif 180 <= degree < 360 or 0 <= degree <= 40:
        print("from north or east to south")
        currentRotation()
        while degree >= 180 or degree < 40:
            currentRotation()
            turn_right()
    elif 50 <= degree < 180:
        print("from north or west to head south")
        currentRotation()
        while degree > 50:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_northWest():
    print("head northwest function")
    if 310 <= degree <= 320:
        print("all ready in head south direction")
    elif 180 <= degree < 310:
        print("from north or east to south")
        currentRotation()
        while degree < 310:
            currentRotation()
            turn_right()
    elif 0 <= degree < 180 or 320 <= degree <= 360:
        print("from north or west to head south")
        currentRotation()
        while degree > 320 or degree < 180:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_southEast():
    print("head south east function")
    if 130 <= degree <= 140:
        print("all ready in head south direction")
    elif 0 <= degree < 130:
        print("from north or east to south")
        currentRotation()
        while degree < 130:
            currentRotation()
            turn_right()
    elif 140 <= degree <= 360:
        print("from north or west to head south")
        currentRotation()
        while degree > 140:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


def head_southWest():
    print("head south west function")
    if 220 <= degree <= 230:
        print("all ready in head south direction")
    elif 0 <= degree < 220:
        print("from north or east to south")
        currentRotation()
        while degree < 220:
            currentRotation()
            turn_right()
    elif 230 < degree <= 360:
        print("from north or west to head south")
        currentRotation()
        while degree > 230:
            currentRotation()
            turn_left()
    else:
        print("no matched direction undefined direction")


currentRotation()
shift_default_direction()
defaultLocation()
head_southWest()
