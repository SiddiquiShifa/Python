# conversion of tuples and tuplefunctions
a="OnePlus","vivo","samsung","redmi","moto","nokia"
print(type(a))
# conversion
a=list(a)
print("After conversion:",type(a))
a.append("Phone")
print(a)
a=tuple(a)
print(a) #notice the braces
print(type(a))
# count
print(a.count("redmi"))
print(a.index("redmi"))