math = int(input("Enter math score: "))
eng = int(input("Enter english score: "))
sci = int(input("Enter science score: "))
phi = int(input("Enter phisics score: "))

total = math + eng + sci + phi
average = total / 4

if 0 <= math <= 20 and 0 <= eng <= 20 and 0 <= sci <= 20 and 0 <= phi <= 20:
    if average >= 18:
        print(average, "A")
    elif average >= 16:
        print(average, "B")
    elif average >= 14:
        print(average, "C")
    elif average >= 10:
        print(average, "D")
    elif average < 10:
        print(average, "Failed")
else:
    print("invalid number")
