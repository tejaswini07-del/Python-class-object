def selfdecor(func):
    def wrapper():
        print("My Info:")
        print("Name: Tejaswini")
        print("Age: 21")
        print("Message: Welcome to my decorated function!")
        func()
        print("..Function finished.")
    return wrapper

@selfdecor
def my_function():
    print("This is the main function doing something important")

my_function()
