a = 12
a1 = 5
a2 = 5.2
b = "Hello"
c = True
d = None
print(a+a1)  # 17
print("type of a", type(a))  # type of a <class 'int'>
print("type of a2", type(a2))  # type of a2 <class 'float'>
print("type of b", type(b))  # type of b < class 'str' >
print("type of c", type(c))  # type of c < class 'bool' >
print("type of d", type(d))  # type of d < class 'bool' >

# collection different/same datatype variable => list
list1 = [8, "2", [a, "1"], True]
print(list1, type(list1))  # [8, '2', [12, '1'], True] <class 'list'>

# dict is like object in js; {'name': 'bhushan', 'age': 25} <class 'dict'>
dict1 = {"name": "bhushan", "age": 25}
print(dict1, type(dict1))
tuple1 = (("a", "b"), ("c", "d"))  # immutable datatype =>tuple
print(tuple1, type(tuple1))  # (('a', 'b'), ('c', 'd')) <class 'tuple'>

# in python all variables are object
