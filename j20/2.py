num1 = int(input("enter first number: "))
op = input("enter operator: ")
num2 = int(input("enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(num1 / num2)
    except Exception as e:
        print(e)
