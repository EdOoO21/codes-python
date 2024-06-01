from sys import stdin


class Matrix:

    def __init__(self, x):
        self.x = [m[:] for m in x]

    def __str__(self):
        string = ''
        for i in self.x:
            string += '\n'
            for n in i:
                string = string + str(n)
                string = string + '\t'

            string = string[:-1]

        return string[1:]

    def size(self):
        return len(self.x), len(self.x[0])

    def __add__(self, other):
        if len(self.x) != len(other.x) or len(self.x[0]) != len(other.x[0]):
            raise
        v = []
        for i in range(len(self.x)):
            v.append([])
        for i in range(0, len(self.x)):
            for n in range(0, len(self.x[0])):
                v[i].append(self.x[i][n] + other.x[i][n])
        return Matrix([x for x in v])

    def __mul__(self, other):
        v = []
        for i in range(len(self.x)):
            v.append([])
        for i in range(0, len(self.x)):
            for n in range(0, len(self.x[0])):
                v[i].append(self.x[i][n] * other)
        return Matrix([x for x in v])

    def __rmul__(self, other):
        return self * other

    


# Task 2 check 2
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
print(2*m1)

