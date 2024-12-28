c = 50


i = 5
while i:
    num = int(input(f"enter your guess: "))
    if num == c:
        print("corecct")
        break
    elif num > c:
        print("too high...")
    else:
        print("too low...")
    i -= 1
