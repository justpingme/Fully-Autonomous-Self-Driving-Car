from firebase import *
from Engine import *


class EngineDirection:
    @staticmethod
    def currentRotation():
        global degree
        rotation = db.child("CurrentRotation").get().val()
        degree = int(rotation)
        print("rotate =", degree)

    """
    North = 0
    NNE = 22
    NE = 45
    ENE = 67
    East = 90
    ESE = 112
    SE = 135
    SSE = 157
    South = 180
    SSW = 202
    SW = 225
    WSW = 247
    West = 270
    WNW = 292
    NW = 315
    NNW = 360
    """

    @staticmethod
    def head_south():
        print("head south function")
        if 175 <= degree <= 185:
            print("all ready in head south direction")
        elif 0 <= degree < 180:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 180:
                EngineDirection.currentRotation()
                turn_right()
        elif 190 <= degree <= 350:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 180:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_north():
        print("head north function")
        if degree >= 355 or degree <= 5:
            print("all ready in head north direction")
        elif 180 <= degree < 355:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 355:
                EngineDirection.currentRotation()
                turn_right()
        elif 5 < degree <= 180:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 5:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_east():
        print("head east function")
        if 85 <= degree <= 95:
            print("all ready in head east direction")
        elif 0 <= degree <= 85:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 85:
                EngineDirection.currentRotation()
                turn_right()
        elif 360 >= degree >= 95:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 95:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_west():
        print("head west function")
        if 265 <= degree <= 275:
            print("all ready in head west direction")
        elif 90 <= degree <= 265:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 265:
                EngineDirection.currentRotation()
                turn_right()
        elif 275 <= degree <= 360 or 0 <= degree >= 90:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree <= 90 or degree >= 275:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_northEast():
        print("head northeast function")
        if 40 <= degree <= 50:
            print("all ready in head south direction")
        elif 180 <= degree < 360 or 0 <= degree <= 40:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree >= 180 or degree < 40:
                EngineDirection.currentRotation()
                turn_right()
        elif 50 <= degree < 180:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 50:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_northWest():
        print("head northwest function")
        if 310 <= degree <= 320:
            print("all ready in head south direction")
        elif 180 <= degree < 310:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 310:
                EngineDirection.currentRotation()
                turn_right()
        elif 0 <= degree < 180 or 320 <= degree <= 360:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 320 or degree < 180:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_southEast():
        print("head south east function")
        if 130 <= degree <= 140:
            print("all ready in head south direction")
        elif 0 <= degree < 130:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 130:
                EngineDirection.currentRotation()
                turn_right()
        elif 140 <= degree <= 360:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 140:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

    @staticmethod
    def head_southWest():
        print("head south west function")
        if 220 <= degree <= 230:
            print("all ready in head south direction")
        elif 0 <= degree < 220:
            print("from north or east to south")
            EngineDirection.currentRotation()
            while degree < 220:
                EngineDirection.currentRotation()
                turn_right()
        elif 230 < degree <= 360:
            print("from north or west to head south")
            EngineDirection.currentRotation()
            while degree > 230:
                EngineDirection.currentRotation()
                turn_left()
        else:
            print("no matched direction undefined direction")

#EngineDirection.currentRotation()