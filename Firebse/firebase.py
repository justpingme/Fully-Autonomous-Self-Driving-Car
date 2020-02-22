import pyrebase

#firebase config
config = {
  "apiKey": "",
  "authDomain": " ",
  "databaseURL": " ",
  "storageBucket": " "
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


