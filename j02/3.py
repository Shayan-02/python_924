num1 = int(input("Enter number1: "))
op = input("Enter operator: ")
num2 = int(input("Enter number2: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator. operator must be +, -, *, /")