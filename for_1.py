# name = "bhuShan"
# for char in name:
#     print(char)
#     if (char.isupper()):
#         print(char, " is upper case")

# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print("\n", color)
#     for char in color:
#         print(char, "-", end="-")


# for k in range(5):
#     print(k + 1, k) # eg. 1 0
startInclude = 2
endExclude = 2
step = 5
for k in range(startInclude, endExclude):
    print(k + 1, k)

for k in range(2, 20, step):
    print(k + 1, k)
# last step output
# 3 2
# 8 7
# 13 12
# 18 17
