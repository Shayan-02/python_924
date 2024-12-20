fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("enter your age: "))

# print("your first name is: " + fname + " and your last name is: " + lname + ".\nyour age is: " + age + " years old")
print("your first name is:", fname, "and your last name is:", lname, ".\nyour age is:", age*2, "years old")
print(f"your first name is: {fname} and your last name is: {lname}.\nyour age is: {age} years old")
print("your first name is: {} and your last name is: {}.\nyour age is: {} years old".format(fname, lname, age))
