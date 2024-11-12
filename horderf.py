def my_decorator(func):
    def wrapper():
        print(func.__name__)
        func()

    return wrapper


@my_decorator
def my_function():
    print("I'm running...")


my_function()
