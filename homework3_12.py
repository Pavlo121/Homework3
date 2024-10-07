class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        def __getattribute__(self, name):
            value = super(new_class, self).__getattribute__(name)
            print(f"Logging: accessed '{name}'")
            return value

        def __setattr__(self, name, value):
            print(f"Logging: modified '{name}'")
            super(new_class, self).__setattr__(name, value)

        new_class.__getattribute__ = __getattribute__
        new_class.__setattr__ = __setattr__

        return new_class


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)
obj.name = "New Python"  
