class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


def analyze_object(obj):
    print("Тип об'єкта:", type(obj))

    print("\nАтрибути і методи:")
    for attr in dir(obj):
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            print(f"{attr}: {type(value)}")


obj = MyClass("World")
analyze_object(obj)





