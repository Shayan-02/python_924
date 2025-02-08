a = input().split()

sums = 0
for i in a:
    sums += int(i)

if sums == 180 and int(a[0]) != 0 and int(a[1]) != 0 and int(a[2]) != 0:
    print("YES")
else:
    print("NO")