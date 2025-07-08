try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
