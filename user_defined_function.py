def calculateFeoMean(a, b):
    answer = (a*b)/(a+b)
    return answer


a = 5
b = 4
c = 8
d = 11
print(calculateFeoMean(a, b))
print(calculateFeoMean(c, d))
# isGreater(a, b) # not defined error


def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")


isGreater(a, b)


def name(fname, mname="Jhon", lname="Whatson"):  # default argument
    print("Hello,", fname, mname, lname)


name("Amy")


name(mname="Peter", lname="Wesker", fname="Jade")  # keyword argument argument


def name2(fname, mname, lname):  # Required arguments:
    print("Hello,", fname, mname, lname)


# name2("Peter", "Quill") # TypeError: name() missing 1 required positional argument: 'lname'


def name3(*name):
    print(type(name))  # <class 'tuple'>
    print("Hello,", name[0], name[1], name[2])


name3("James", "Buchanan", "Barnes")


def name4(**name):
    print(type(name))  # <class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])


name4(mname="Buchanan", lname="Barnes", fname="James")


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    # return 7
    return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)
