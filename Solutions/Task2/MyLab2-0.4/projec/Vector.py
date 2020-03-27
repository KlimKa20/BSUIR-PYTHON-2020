import math


class Vector:

    def __init__(self, value):
        if len(value) < 1 or isinstance(value, str):
            print("It's not vector")
            raise
        self.value= list(map(int, value))

    def __add__(self, other):

        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi + wi for vi, wi in zip(self.value, other.value)])
        else:
            print("error")

    # def __iadd__(self, other):
    #     if isinstance(other, Vector)and len(other.value)==len(self.value):
    #         self.value = [vi + wi for vi, wi in zip(self.value, other.value)]
    #         return self
    #     else:
    #         print("error")

    def __mul__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi * wi for vi, wi in zip(self.value, other.value)])
        elif isinstance(other, int) or isinstance(other, float):
            self.value=[i * other for i in self.value]
            return self
        else:
            print("error")

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.value = [i * other for i in self.value]
            return self
        else:
            print("error")

    # def __imul__(self, other):
    #     if isinstance(other, Vector)and len(other.value)==len(self.value):
    #         self.value=[vi * wi for vi, wi in zip(self.value, other.value)]
    #         return self
    #     elif isinstance(other, int) or isinstance(other, float):
    #         self.value=[i * other for i in self.value]
    #         return self
    #     else:
    #         print("error")

    def __sub__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi - wi for vi, wi in zip(self.value, other.value)])
        else:
            print("error")

    # def __isub__(self, other):
    #     if isinstance(other, Vector)and len(other.value)==len(self.value):
    #         self.value = [vi - wi for vi, wi in zip(self.value, other.value)]
    #         return self
    #     else:
    #         print("error")

    def __repr__(self):
        return ','.join([str(x) for x in self.value])

    def __getitem__(self, item):
        return self.value[item]

    def len(self):
        return math.sqrt(sum(vi ** 2 for vi in self.value))

    def __lt__(self, other):
        return True if self.len() < other.len() else False

    def __le__(self, other):
        return True if self.len() <= other.len() else False

    def __eq__(self, other):
        return True if self.len() == other.len() else False

    def __ne__(self, other):
        return True if self.len() != other.len() else False

    def __gt__(self, other):
        return True if self.len() > other.len() else False

    def __ge__(self, other):
        return True if self.len() >= other.len() else False


