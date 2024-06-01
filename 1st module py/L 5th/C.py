import sys


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a1):
        return Point3D(self.x + a1.x, self.y + a1.y, self.z + a1.z)

    def __iadd__(self, a1):
        return Point3D(self.x + a1.x, self.y + a1.y, self.z + a1.z)

    def __eq__(self, a1):
        return (self.x == a1.x) and (self.y == a1.y) and (self.z == a1.z)

    def __ne__(self, a1):
        return not ((self.x == a1.x) and (self.y == a1.y) and (self.z == a1.z))

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    @staticmethod
    def dist(self, a1):
        return (((self.x - a1.x) ** 2) + ((self.y - a1.y) ** 2) + ((self.z - a1.z) ** 2)) ** 0.5
