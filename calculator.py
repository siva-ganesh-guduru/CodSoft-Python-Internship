import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot perform modulus with zero!"
    return x % y

def floor_divide(x, y):
    if y == 0:
        return "Error: Cannot perform floor division by zero!"
    return x // y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number!"
    return math.sqrt(x)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice not in ('1', '2', '3', '4', '5', '6', '7', '8'):
        print("Invalid choice")
        return

    if choice == '8':
        num = float(input("Enter the number: "))
        result = square_root(num)
        print("Result:", result)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = exponentiate(num1, num2)
        elif choice == '6':
            result = modulus(num1, num2)
        else:
            result = floor_divide(num1, num2)

        print("Result:", result)

if __name__ == "__main__":
    calculator()