def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_nine():
    print("Нет аргументов")


print_two("Михаил", "Василий")
print_two_again("Вася", "Маруся")
print_one("Петя")
print_nine()
