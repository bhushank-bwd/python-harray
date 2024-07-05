name = "Bhushan"
print(name[0])  # name[7] will give error

text = '''
Exercitation velit dolor aute laborum elit sint veniam ex reprehenderit.
Incididunt exercitation irure incididunt ad commodo veniam elit consequat. Duis occaecat adipisicing enim sint commodo nulla irure quis 
exercitation. Ut ea ullamco adipisicing ad dolor. Laborum ullamco anim mollit aute reprehenderit ipsum in aute ullamco ad esse.
'''  # this is multiline string

for char in name:
    print(char)

nameLen = len(name)
print(nameLen)
startWithInclude = 2
endWithExclude = 5
print(name[startWithInclude:endWithExclude])  # ush

startWithInclude = -6  # nameLen-startWithInclude 1
endWithExclude = -2  # nameLen-endWithExclude = 5

print(name[startWithInclude:endWithExclude])  # hush
