start = int(input("enter start number: "))
end = int(input("enter end number: "))

c = 1
# for i in range(start, end + 1):
#     if i % 3 == 0:
#         print(c , ":",i)
#         c += 1
i = start
while i < end + 1:
    if i % 3 == 0:
        print(c , ":",i)
        c += 1
    i += 1