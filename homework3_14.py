class TypeCheckedMeta(type):
    def __new__(cls, name, bases, attrs):
        type_hints = {}
        for attr, value in attrs.items():
            if not attr.startswith('__') and isinstance(value, type):
                type_hints[attr] = value

        attrs['_type_hints'] = type_hints
        return super().__new__(cls, name, bases, attrs)

    def __setattr__(cls, name, value):
        if name in cls._type_hints:
            expected_type = cls._type_hints[name]
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Для атрибута '{name}' очікується тип '{expected_type.__name__}', але отримано '{type(value).__name__}'."
                )
        super().__setattr__(name, value)

class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"
p.age = "30"

