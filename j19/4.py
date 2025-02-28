num1 = int(input("enter num1: "))
op = input("enter op: ")
num2 = int(input("enter num2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        num1 / num2
    except ZeroDivisionError:
        print("num2 must be a number except 0")
else:
    print("invalid input")