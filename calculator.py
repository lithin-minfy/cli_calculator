def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


n = 7
numbers = []
count = 0

print(f"Please enter {n} numbers:")

while count < n:
    try:
        user_input = int(input(f"Enter number {count + 1}: "))
        numbers.append(user_input)
        count += 1
    except ValueError:
        print(" Invalid input. Please enter an integer.")

print("Entered numbers:", numbers)


valid_operations = ['+', '-', '*', '/']
operation = input("Enter operation (+, -, *, /): ").strip()

if operation not in valid_operations:
    print(f"Invalid operation. Please enter one of {valid_operations}")
else:
    result = numbers[0]
    try:
        for i in range(1, n):
            if operation == "+":
                result = add(result, numbers[i])
            elif operation == "-":
                result = sub(result, numbers[i])
            elif operation == "*":
                result = mult(result, numbers[i])
            elif operation == "/":
                result = div(result, numbers[i])
    except ZeroDivisionError as zde:
        print(" Error:", zde)
    else:
        print(f" Result is: {result}")
