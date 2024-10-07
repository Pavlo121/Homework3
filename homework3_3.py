import inspect
import importlib


def analyze_module(module_name):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Модуль '{module_name}' не знайдено.")
        return

    print("Функції:")
    functions = [name for name, obj in inspect.getmembers(module, inspect.isfunction)]
    if functions:
        for name in functions:
            func = getattr(module, name)
            print(f"- {name}{inspect.signature(func)}")
    else:
        print("- <немає функцій у модулі>")

    print("\nКласи:")
    classes = [name for name, obj in inspect.getmembers(module, inspect.isclass) if obj.__module__ == module_name]
    if classes:
        for name in classes:
            print(f"- {name}")
    else:
        print(f"- <немає класів у модулі {module_name}>")


analyze_module("math")
