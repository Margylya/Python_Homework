def my_func(a, b):
    try:
        a = int(a)
        b = int(b)
        division = a / b
    except ValueError:
        return ("Enter number!!")
    except ZeroDivisionError:
        return ("Enter not zero number!!")
    return (division)
print(my_func(input("Enter one number"), input("Enter two number")))



