class Point(object):
    def __init__(self, x, y):

        if type(x) != int or type(y) != int:
            raise TypeError("Point Values not of correct type")

        self._x = x
        self._y = y

    def getX(self):
        return self._y

    def setX(self, x):
        if type(x) != int:
            raise TypeError("Point Values not of correct type")
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        if type(y) != int:
            raise TypeError("Point Values not of correct type")
        self._y = y

    def __str__(self):
        return ("X: %d Y: %d" % (self._x, self._y))

    def __eq__(self, otherpoint):
        if self._x == otherpoint.x and self._y == otherpoint.y:
            return True
        else:
            return False

    x = property(getX, setX)
    y = property(getY, setY)


class Rectangle(object):

    def __init__(self, topx, topy, bottomx, bottomy):
        try:
            self._topLeft = Point(topx, topy)
        except TypeError:
            raise RectangleError("Top Left Point could not be instantiated")

        try:
            self._bottomRight = Point(bottomx, bottomy)
        except TypeError:
            raise RectangleError("Top Left Point could not be instantiated")

    def getTopLeft(self):
        return self._topLeft

    def setTopLeft(self, newPoint):
        self._topLeft = newPoint

    def getBottomRight(self):
        return self._bottomRight

    def setBottomRight(self, newPoint):
        self._bottomRight = newPoint

    def __str__(self):
        return ("%s %s" % (str(self._topLeft), str(self._bottomRight)))

    topLeft = property(getTopLeft, setTopLeft)
    bottomRight = property(getBottomRight, setBottomRight)


class Square(Rectangle):

    def __init__(self, topx, topy, bottomx, bottomy):
        if bottomx - topx != bottomy - topy:
            raise SquareError("Sides not even")
        Rectangle.__init__(self, topx, topy, bottomx, bottomy)


class RectangleError(Exception):
    pass


class SquareError(Exception):
    pass


def testSquare():
    try:
        square = Square(10, 10, 10, 20)
    except SquareError:
        print("Sides not even")

    try:
        square = Square(10, 10, 20, 20)
    except SquareError:
        print("Sides not even")

    print(square)

    try:
        point1 = Point(10, 10)
    except TypeError:
        print("Wrong types passed for point parameters")
    square.bottomRight = point1

    print(square)


def testRectangle():
    try:
        rectangle1 = Rectangle(10, 10, 20, 20)
    except RectangleError:
        print("Error instantiating the Rectangle")
    print(rectangle1)

    try:
        point1 = Point(10, 10)
    except TypeError:
        print("Wrong types passed for point parameters")
    rectangle1.bottomRight = point1

    print(rectangle1.topLeft, rectangle1.bottomRight)


def testPoint():
    try:
        point0 = Point("ten", "ten")
    except TypeError:
        print("Wrong types passed for point parameters")

    try:
        point1 = Point(10, 10)
    except TypeError:
        print("Wrong types passed for point parameters")

    try:
        point2 = Point(20, 20)
    except TypeError:
        print("Wrong types passed for point parameters")

    print(point1)
    print(point1.x, " ", point1.y)
    print(point1 == point2)

    try:
        point1.x = 20
        point1.y = 20
    except TypeError:
        print("Wrong types passed for point parameters")

    print(point1 == point2)


if __name__ == "__main__":
    testPoint()
    testRectangle()
    testSquare()
