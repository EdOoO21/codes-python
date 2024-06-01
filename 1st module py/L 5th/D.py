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

    def axial_symmetric(self, axis, inplace=False):
        if type(axis) is not str:
            raise Point3DError(f'invalid axis type: {type(axis)}')
        if axis != 'x' and axis != 'y' and axis != 'z':
            raise Point3DError(f'invalid axis name: {axis}')
        if axis == 'x' or axis == 'y' or axis == 'z':
            if inplace:
                if axis == 'y':
                    self.x, self.y, self.z = -self.x, self.y, -self.z
                    return self.x, self.y, self.z
                elif axis == 'x':
                    self.x, self.y, self.z = self.x, -self.y, -self.z
                    return self.x, self.y, self.z
                else:
                    self.x, self.y, self.z = -self.x, -self.y, self.z
                    return self.x, self.y, self.z
            else:
                if axis == 'y':
                    return Point3D(-self.x, self.y, -self.z)
                elif axis == 'x':
                    return Point3D(self.x, -self.y, -self.z)
                else:
                    return Point3D(-self.x, -self.y, self.z)

    @staticmethod
    def dist(self, a1):
        return (((self.x - a1.x) ** 2) + ((self.y - a1.y) ** 2) + ((self.z - a1.z) ** 2)) ** 0.5


class Point3DError(TypeError):

    def __init__(self, text):
        self.e = text


p1 = Point3D(1, 2, 3)

print(p1.axial_symmetric('yw', False))

print(Point3DError.e)
