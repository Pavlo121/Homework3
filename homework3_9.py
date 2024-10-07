class DynamicProperties:
    def __init__(self):
        self.properties = {}

    def add_property(self, name, default_value):
        self.properties[name] = default_value

        def getter(self):
            return self.properties[name]

        def setter(self, value):
            self.properties[name] = value

        setattr(self.__class__, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)
obj.name = "Python"
print(obj.name)


