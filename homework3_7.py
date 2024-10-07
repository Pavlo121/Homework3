def log_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            def wrapper(self, *args, **kwargs):
                print(f"Logging: {attr_name} called with {args}")
            setattr(cls, attr_name, wrapper)
    return cls


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  
obj.subtract(5, 3)
