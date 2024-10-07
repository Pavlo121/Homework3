class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return lambda *args, **kwargs: self._log_and_call(name, *args, **kwargs)

    def _log_and_call(self, name, *args, **kwargs):
        # Логируем вызов и вызываем оригинальный метод
        print(f"Calling method:\n{name} with args: {args}")
        return getattr(self._obj, name)(*args, **kwargs)

class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"

obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))

