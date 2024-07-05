a = "1"
a1 = "1a"

b = "5"

print(a+b)  # 15
print(int(a)+int(b))  # 6
# print(int(a1))  # error invalid literal for int() with base 10: '1a'

c = 8.9
d = 5
print(c+d)  # converts 5 to float i.e. implicit casting converts lower data type to higher data type to prevent datatype

a = input("Enter name")  # always give string
print("your name : "+a)

b = input("Enter first number")
c = input("Enter second number")
print(b+c)
print(int(c)+int(b))
