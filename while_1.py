# i = 0
# while (i < 3):
#     print(i)
#     i = i+1

# j = 5
# while (j > 0):
#     print(j)
#     j = j-1

# a = int(input("Enter input: "))

# while (a <= 10):
#     if (a == 10):
#         a = int(input("Enter input: "))
#         continue
#     if (a == 0):
#         break
#     print(a)
#     a = int(input("Enter input: "))

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 5 == 0):
        break
