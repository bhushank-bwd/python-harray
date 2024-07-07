a = int(input("Enter input: "))

print("Your answer is ", a)

if (a < 16):
    print("you can't drive")
elif (a < 18):
    print("you can drive scooty only")
    if (a == 17):
        print("you are 17")
    else:
        print("you are", a)
else:
    print("you can drive all vehicle")
