import sys


class ExtendedList(list):
    def __init__(self, b):

        self.b = b
        self.reversed = list(reversed(b))
        self.first = b[0]
        self.last = b[-1]
        self.size = len(b)
    print('class used')


l = ExtendedList([1, 2, 3])
print(l.reversed)
print(l.first)
l.first = 0
print(l)
l.append(4)
print(l.last)
l.size = 2
print(l)