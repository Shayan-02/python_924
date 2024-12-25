c = 70

for i in range(1, 4):
    num = int(input("enter your choice(1, 100): "))
    if num == c:
        print("correct")
        break
    elif num > c:
        print("too high...")
    else:
        print("too low...")
