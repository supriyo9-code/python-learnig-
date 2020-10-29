import pickle
#pickleing a python object
# cars = ["Audi", "BMW", "Farari", "Tesla"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


#depickle
file = "mycar.pkl"
fileobj =open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
