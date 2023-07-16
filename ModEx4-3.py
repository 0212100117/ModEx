class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):

        return self.x

    def getY(self):

        return self.y

    def __str__(self):
        return "<" + str(self.getX()) + ', ' + str(self.getY()) + ">"

    def __eq__(self, coordinates2):
        if coordinates2.x == self.x and coordinates2.y == self.y:
            return True
        else:
            return False

    def __repr__(self):
        return str(print("Coordinate", str((self.x, self.y))))


coord1 = Coordinate(10, 20)
coord2 = Coordinate(10, 20)
print(coord1 == coord2)
eval(repr(coord1))
