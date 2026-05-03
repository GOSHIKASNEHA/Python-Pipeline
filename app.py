def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1-4): "))
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(x, y))
    elif choice == 2:
        print("Result:", subtract(x, y))
    elif choice == 3:
        print("Result:", multiply(x, y))
    elif choice == 4:
        print("Result:", divide(x, y))
    else:
        print("Invalid choice")


print("Lab 3 Git modification")
print("This is wrong commit")