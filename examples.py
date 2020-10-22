# x = 8 = 5  SyntaxError: cannot assign to literal
# y = 5 / 0 ZeroDivisionError: division by zero


def fuctorial(n):
    """Calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * fuctorial(n - 1)


try:
    print(fuctorial(999))
except RecursionError:
    print("This program can not calculate factorials that large!\n")
except ZeroDivisionError:
    print("Are you stupid dividing by zero???")

print("Program terminating!")


