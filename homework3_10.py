class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            instance = super().__call__(*args, **kwargs)
            cls.instances[cls] = instance
            return instance
        return cls.instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)
