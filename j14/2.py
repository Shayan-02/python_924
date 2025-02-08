# دریافت ورودی از کاربر
num1 = input().split()
num2 = input().split()

# محاسبه تعداد 1های هم‌موقع
count = 0
for i in range(8):
    if num1[i] == '1' and num2[i] == '1':
        count += 1

print(count)
