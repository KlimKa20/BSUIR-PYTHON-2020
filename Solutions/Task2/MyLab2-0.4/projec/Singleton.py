class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(SingletonMeta, self).__call__(*args, **kwargs)
        else:
            print("The connection is established")
        return self._instances[self]


class Singleton(metaclass=SingletonMeta):

    def __init__(self, name):
        self.name = name


