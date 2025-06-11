# its unique if same element is double it wont print twice 
a={"First",2,"Second",2}
print(a,type(a))

# set functions
a.add("New")
print(a)

# pop -randomly removes
a.pop()
print(a)

# remove is used particulary removing a value
# a.remove("New")
# print(a)

# discard
a.discard("Second")
print(a)

# copy
a={"S",1}
b=a.copy()
print(b)

# disjoint~ two sets have no elements in common. I
a = {1, 2, 3}
b = {4, 5, 6,}
c = {3, 4, 5}
print(a.isdisjoint(b)) #thers no COMMON element
print(b.isdisjoint(c))

# issubset
b = {4, 5, 6,3,1,4}
c = {3, 4, 5}

print(a.issubset(b))
print(c.issubset(b),"~subset")

# supperset
print(b.issuperset(c),"~supperset")

# clear
print(a.clear())
print(a)

# union
a = {1, 2, 3}
b = {4, 5, 6,}
print(a.union(b))

# difference
b = {4, 5, 6,}
c = {3, 4, 5}
print(b.difference(c))
print(c.difference(b))

# interecton
print(b.intersection(c))
