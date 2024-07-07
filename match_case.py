a = int(input("Enter input: "))

print("Your answer is ", a)
# instead of switch here match and break is not in python
match a:
    case 0:
        print("not possible drive")
    case 16:
        print("SSC completed")
    case 18:
        print("you apply to drive")
    case 21:
        print("you can marry")
    case _ if a != 90:
        print(a, "is not 90")
    case _:
        print(a)
