for i in range(1, 21):
    if i == 10 or i == 14:
        i += 5
        continue
    print(i, end="\t")

print()
print()
j = 1
while j <= 20:
    if j == 10 or j == 14:
        j += 2
        continue
    print(j, end="\t")
    j += 1
