import sys


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, a1):
        return Vector(self.x + a1.x, self.y + a1.y)

    def __sub__(self, a1):
        return Vector(self.x - a1.x, self.y - a1.y)

    def __mul__(self, a1):
        return Vector(self.x * a1, self.y * a1)

    def __rmul__(self, a1):
        return Vector(self.x * a1, self.y * a1)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, a1):
        return (self.x == a1.x) and (self.y == a1.y)

    def __ne__(self, a1):
        return not ((self.x == a1.x) and (self.y == a1.y))

    def reverse(self):
        return Vector(-self.x, -self.y)

    @staticmethod
    def make_vector(p1: tuple, p2: tuple):
        return Vector(p2[0] - p1[0], p2[1] - p1[1])
