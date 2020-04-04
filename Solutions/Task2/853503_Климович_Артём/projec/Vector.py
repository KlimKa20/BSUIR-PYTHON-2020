import math


class Vector:

    def __init__(self, value):
        if len(value) < 1 or isinstance(value, str):
            raise ValueError("Несоответствующее значение")
        if not all(map(lambda i: isinstance(i, int), value)):
            raise ValueError("Несоответствующее значение")
        self.value = list(map(int, value))

    def __add__(self, other):

        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi + wi for vi, wi in zip(self.value, other.value)])
        else:
            raise ValueError("Некоректные аргументы")

    def __mul__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi * wi for vi, wi in zip(self.value, other.value)])
        elif isinstance(other, int) or isinstance(other, float):
            self.value=[i * other for i in self.value]
            return self
        else:
            raise ValueError("Некоректные аргументы")

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.value = [i * other for i in self.value]
            return self
        else:
            raise ValueError("Некоректные аргументы")

    def __sub__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return Vector([vi - wi for vi, wi in zip(self.value, other.value)])
        else:
            raise ValueError("Некоректные аргументы")

    def __repr__(self):
        return ','.join([str(x) for x in self.value])

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.value[item]
        else:
            raise ValueError("Некоректные аргументы")

    def len(self):
        return math.sqrt(sum(vi ** 2 for vi in self.value))

    def __lt__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() < other.len() else False
        else:
            raise ValueError("Некоректные аргументы")

    def __le__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() <= other.len() else False
        else:
            raise ValueError("Некоректные аргументы")

    def __eq__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() == other.len() else False
        else:
            raise ValueError("Некоректные аргументы")

    def __ne__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() != other.len() else False
        else:
            raise ValueError("Некоректные аргументы")

    def __gt__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() > other.len() else False
        else:
            raise ValueError("Некоректные аргументы")

    def __ge__(self, other):
        if isinstance(other, Vector) and len(other.value) == len(self.value):
            return True if self.len() >= other.len() else False
        else:
            raise ValueError("Некоректные аргументы")



