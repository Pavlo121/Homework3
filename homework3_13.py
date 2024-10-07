class AutoMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        for attr in attrs:
            if not attr.startswith('__'):
                def getter(self, attr=attr):
                    return getattr(self, f'_{attr}')

                def setter(self, value, attr=attr):
                    setattr(self, f'_{attr}', value)

                setattr(new_class, f'get_{attr}', getter)
                setattr(new_class, f'set_{attr}', setter)

                setattr(new_class, f'_{attr}', attrs[attr])

        return new_class


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
