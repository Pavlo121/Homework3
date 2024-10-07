def call_function(obj, method_name, *args):
    return getattr(obj, method_name)(*args)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()

print(call_function(calc, 'add', 10, 5))
print(call_function(calc, 'subtract', 10, 5))