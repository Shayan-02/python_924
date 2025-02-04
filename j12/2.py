import random as r

start = int(input("enter start number: "))
end = int(input("enter end number: "))

a = r.randint(start, end)
for i in range(len(str(a)) * 2):
    x = int(input(f"enter a number{(len(str(a)) * 2) - i}: "))
    if x == a:
        print("you win")
        break
    else:
        print("you lose")