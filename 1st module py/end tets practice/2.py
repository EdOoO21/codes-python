import sys


class CommonProperties:
    def __init__(self, data):
        self.data = data

    @property
    def size(self):
        return len(self.data)

    @property
    def max_value(self):
        if type(self.data) != list:
            b = self.data.keys()
            return max(b)
        else:
            return max(self.data)

    @property
    def min_value(self):
        if type(self.data) != list:
            b = self.data.keys()
            return min(b)
        else:
            return min(self.data)


class DictProperties(CommonProperties):
    @property
    def max_value(self):
        try:
            a = self.data.values()
            b = self.data.keys()
            return max(max(a), max(b))
        except Exception:
            try:
                b = self.data.keys()
                return max(b)
            except Exception:
                raise TypeError

    @property
    def min_value(self):
        try:
            a = self.data.values()
            b = self.data.keys()
            return min(min(a), min(b))
        except Exception:
            try:
                b = self.data.keys()
                return min(b)
            except Exception:
                raise TypeError


class CustomList(CommonProperties):
    def __str__(self):
        return f'My CustomList data {self.data}'

    @property
    def max_value(self):
        return max(self.data)

    @property
    def min_value(self):
        return min(self.data)


class CustomDict(DictProperties, CommonProperties):
    def __str__(self):
        return f'My CustomDict data {self.data}'


exec(sys.stdin.read())