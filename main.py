"""Metaclass Singleton"""


class SingletonMeta(type):
    """Metaclass"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Singleton"""
    def __init__(self, data):
        self.data = data


s1 = Singleton("Instance 1")
s2 = Singleton("Instance 2")


print(s1.data)
print(s2.data)
print(s1 == s2)
