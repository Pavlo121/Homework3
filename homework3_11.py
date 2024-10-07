class LimitedAttributesMeta(type):
    def __init__(cls, name, bases, attrs):
        user_defined_attrs = {key: value for key, value in attrs.items() if not key.startswith('__')}

        if len(user_defined_attrs) > 3:
            raise TypeError(f"Клас {name} не може мати більше 3 атрибутів.")
        super().__init__(name, bases, attrs)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    #attr4 = 4  # Викличе помилку


obj = LimitedClass()
