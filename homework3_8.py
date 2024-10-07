def analyze_inheritance(cls):
    class_methods = set(dir(cls))

    inherited_methods = {}

    for base in cls.__bases__:
        base_methods = set(dir(base))

        inherited = class_methods.intersection(base_methods)

        for method in inherited:
            if method not in inherited_methods:
                inherited_methods[method] = base.__name__

    if inherited_methods:
        print(f"Клас {cls.__name__} наслідує:")
        for method, base_class in inherited_methods.items():
            print(f"- {method} з {base_class}")

class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)

