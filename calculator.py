def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Exponentiation (**)")
print("7. Modulus (%)")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", floor_divide(num1, num2))
elif choice == '6':
    print("Result:", exponentiate(num1, num2))
elif choice == '7':
    print("Result:", modulus(num1, num2))
else:
    print("Invalid input! Please select a valid operation.")