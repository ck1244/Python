#Colin Kelleher

import unittest

class Vehicle(object):
    def __init__(self,engineCapacity,numberOfDoors,licence):

            if type(engineCapacity) is not int or type(numberOfDoors) is not int:
                raise GeneralTypeError ("Engine Capacity/Number of Doors not of correct type")

            self._engineCapacity = engineCapacity
            self._numberOfDoors = numberOfDoors
            self._licence = licence

    def setEngineCapacity(self,engineCapacity):
        if type(engineCapacity) is not int:
            raise GeneralTypeError ("Engine Capacity not of correct type")
        self._engineCapacity = engineCapacity

    def getEngineCapacity(self):
        return self._engineCapacity

    def setNumberOfDoors(self,numberOfDoors):
        if type(numberOfDoors) is not int:
            raise GeneralTypeError ("Number of Doors not of correct type")
        self._numberOfDoors = numberOfDoors

    def getNumberOfDoors(self):
        return self._numberOfDoors

    def __str__(self):
        return ("\nEngine Capacity: %i\nNumber of Doors: %i " % (self._engineCapacity, self._numberOfDoors))

class Van(Vehicle):
    def __init__(self,engineCapacity,numberOfDoors,cargoCapacity,licence):
        Vehicle.__init__(self,engineCapacity,numberOfDoors,licence)
        self._cargoCapacity = cargoCapacity

        if licence._points > 0:
            raise licencePointsError('Too many points on licence')

        if licence._licenceType < 3:
            raise licenceTypeError('You do not have the correct Licence')


    def getCargoCapacity(self):
        return self._cargoCapacity

    def setCargoCapacity(self,cargoCapacity):
        if type(cargoCapacity) is not int:
            raise GeneralTypeError("Cargo Capacity not of correct type")

        self._cargoCapacity = cargoCapacity


    def __str__(self):
        return ("\nEngine Capacity: %i\nNumber of Doors: %i\nCargo Capacity: %i " % (self._engineCapacity, self._numberOfDoors,self._cargoCapacity))

class Car(Vehicle):
    def __init__(self,engineCapacity,numberOfDoors,numberOfSeats,towBar,licence):
        Vehicle.__init__(self,engineCapacity,numberOfDoors,licence)

        if licence._points > 2:
            raise licencePointsError('Too many points on licence')

        if licence._licenceType < 1:
            raise licenceTypeError('You do not have the correct Licence')


        self._numberOfSeats = numberOfSeats
        self._towBar = towBar

    def getNumberOfSeats(self):
        return self._numberOfSeats

    def setNumberOfSeats(self,numberOfSeats):
        if type(numberOfSeats) is not int:
            raise GeneralTypeError ("Number of Seats not of correct type")

        self._numberOfSeats = numberOfSeats

    def getTowBar(self):
        return self._towBar

    def setTwoBar(self,towBar):
        if type(towBar) is not bool:
            raise GeneralTypeError ("Tow Bar not of correct type")
        self._towBar = towBar

    def __str__(self):
        return ("\nEngine Capacity: %i\nNumber of Doors: %i\nNumber of Seats: %i\nTowbar: %r  " %(self._engineCapacity, self._numberOfDoors,self._numberOfSeats,self._towBar))


class licence(object):
    def __init__(self, points,licenceType):
        if type(points) is not int or type(licenceType) is not int:
            raise GeneralTypeError("Points / Licence Type is not of the correct type")
        self._points = points
        self._licenceType = licenceType


    def setPoints(self,points):
        if type(points) is not int:
            raise GeneralTypeError ("Licence Points not of correct type")

        self._points = points

    def getPoints(self):
        return self._points

    def setType(self,type):
        if type(type) is not int:
            raise GeneralTypeError ("Licence Type not of correct type")
        self._licenceType = type

    def getType(self):
        return self._licenceType

    def __str__(self):
        return ("Points on Licence: %i, Licence Type: %i" % (self._points,self._licenceType))



class licenceTypeError(Exception):
    pass

class licencePointsError (Exception):
    pass

class GeneralTypeError(Exception):
    pass

class LicenceTestMethods(unittest.TestCase):
    def testVan(self):
        with self.assertRaises(TypeError):
            lic = licence(2,3)
            Van(100,4,300,lic)
    def testVan1(self):
            self.assertRaises(TypeError)
            lic = licence(0,2)
            Van(100,4,300,lic)
    def testVan2(self):
            self.assertRaises(TypeError)
            lic = licence(4,3)
            Van(100,4,300,lic)
    def testVan3(self):
            self.assertRaises(TypeError)
            lic = licence(0,3)
            Van(100,4,300,lic)
    def testCar(self):
            self.assertRaises(TypeError)
            lice = licence(0,3)
            Car(1000,3,4,True,lice)
    def testCar1(self):
            self.assertRaises(TypeError)
            lice = licence(2,0)
            Car(1000,3,4,True,lice)
    def testCar3(self):
        self.assertRaises(TypeError)
        lice = licence(3, 1)
        Car(1000, 3, 4, True, lice)
    def testlicence(self):
        self.assertRaises(TypeError)
        licence('abc','abc')







if __name__ == "__main__":
    unittest.main()





