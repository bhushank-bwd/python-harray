string_1 = "BhuShan"
# print(string_1.upper())  # BHUSHAN
# print(string_1.lower())  # bhushan
# print(string_1.swapcase())  # bHUsHAN
str2 = " Silver Spoon "
str3 = "!!! Silver Spoon !!!"
# print(str2.strip())  # Silver Spoon
# print(len(str2.rstrip()), len(str2), len(str2.lstrip()))  # 13 14 13
# print(str2.rstrip())  # Silver Spoon
# print(str2.lstrip())  # Silver Spoon

# print(str3.rstrip("!"))  # !!! Silver Spoon
# print(str3.lstrip("!"))  # Silver Spoon !!!

# print(str2.replace("Sp", "M"))  # Silver Moon

# print(str2.split(" "))  # ['', 'Silver', 'Spoon', '']

str1 = "hello"
capStr1 = str1.capitalize()  # Hello
# print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
# print(capStr2)  # Hello world

str1 = "Welcome to the Console!!!"
# The center() method aligns the string to the center as per the parameters given by the user.
# print(str1.center(50))
#             Welcome to the Console!!!

str2 = "Abracadabra"
countStr = str2.count("a")  # case sensitive
# print(countStr)  # 4

str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))  # True
# print(str1.startswith("!!!"))  # False

startIncludes = 4
endExcludes = 10
# print(str1.endswith("to", 4, 10))  # ome to => True

str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))  # 10 i.e. position

# this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str1 = "He's name is Dan. He is an honest man."
# print(str1.find("Daniel"))  # -1

str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))  # 13
# print(str1.index("DanGo"))  # ValueError: substring not found

str1 = "WelcomeToTheConsole12"
str2 = "WelcomeToTheConsole#12"
# return only contains A-Z, a-z, 0-9.; True False
# print(str1.isalnum(), str2.isalnum())

str1 = "Welcome"
str2 = "Welcome123"
# return only contains A-Z, a-z; True False
# print(str1.isalpha(), str2.isalpha())

str1 = "hello world"
str2 = "hEllo world"
# print(str1.islower(), str2.islower())  # True False

str1 = "We wish you a Merry Christmas"
str2 = "We wish \nyou a Merry Christmas"
# print(str1.isprintable(), str2.isprintable())  # True False

str1 = "        "  # using Spacebar
# print(str1.isspace())  # True
str2 = "        "  # using Tab
str3 = "avb"  #
# print(str2.isspace(), str3.isspace())  # True False

str1 = "World Health Organization"
str2 = "World health Organization"
# print(str1.istitle(), str2.istitle())  # True False

str1 = "ABC"
str2 = "abc"
# print(str1.isupper(), str2.isupper())  # True False
# print(str1.islower(), str2.islower())  # False True
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())  # He'S Name Is Dan. Dan Is An Honest Man.
