a = input().split()

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])

if a1 + a2 + a3 == 180 and a1 != 0 and a2 != 0 and a3 != 0:
    print("Yes")
else:
    print("No")