from sys import stdin


class MatrixError(BaseException):
    def __init__(self, a, b):
        self.matrix1, self.matrix2 = a, b


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
            raise MatrixError(self, other)
        else:
            v = []
            for i in range(len(self.x)):
                v.append([])
            for i in range(0, len(self.x)):
                for n in range(0, len(self.x[0])):
                    v[i].append(self.x[i][n] + other.x[i][n])
            return Matrix([x for x in v])

    def __mul__(self, other):
        if (type(other) is int) or (type(other) is float):
            v = []
            for i in range(len(self.x)):
                v.append([])
            for i in range(0, len(self.x)):
                for n in range(0, len(self.x[0])):
                    v[i].append(self.x[i][n] * other)
            return Matrix([x for x in v])

        else:
            if len(self.x[0]) != len(other.x):
                raise MatrixError(self, other)
            v = [[0 for _ in range(other.size()[1])] for _ in range((self.size()[0]))]
            for i in range(self.size()[0]):
                for n in range(other.size()[1]):
                    for k in range(self.size()[1]):
                        v[i][n] += self.x[i][k] * other.x[k][n]
                        # v[i][n] = sum([(self.x[i][x] + other.x[x][n]) for x in range(self.size()[1])])

            return Matrix(v)

    def __rmul__(self, other):
        return self * other

    def transpose(self):
        v = [[0 for _ in range(len(self.x))] for _ in range(len(self.x[0]))]
        for i in range(len(self.x)):
            for n in range(len(self.x[0])):
                v[n][i] = self.x[i][n]

        self.x = [x for x in v]
        return self

    @staticmethod
    def transposed(self):
        v = [[0 for _ in range(len(self.x))] for _ in range(len(self.x[0]))]
        for i in range(len(self.x)):
            for n in range(len(self.x[0])):
                v[n][i] = self.x[i][n]

        return Matrix([x for x in v])

