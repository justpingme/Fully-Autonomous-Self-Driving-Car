import pyrebase

#firebase config
config = {
  "apiKey": "AIzaSyAc8-wcVf3ZysBh4iAJvcr1wijTSzr_ynk",
  "authDomain": "android-rider-app-41d08.firebaseapp.com",
  "databaseURL": "https://android-rider-app-41d08.firebaseio.com",
  "storageBucket": "android-rider-app-41d08.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

destinationDatabase = db.child("CurrentRider").child("Destination").get()
totalItems = dict(destinationDatabase.val())
print(totalItems.values())
Dlat = totalItems["latitude"]
Dlong = totalItems["longitude"]
print("latitude = {} \nlongtitude = {}".format(Dlat, Dlong))

pickupDatabase = db.child("CurrentRider").child("PickupLocation").get()
alluser = dict(pickupDatabase.val())
print(alluser.values())
Plat = alluser["latitude"]
Plong = alluser["longitude"]
print("latitude = {} \nlongtitude = {}".format(Plat, Plong))


