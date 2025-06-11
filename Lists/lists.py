a=["Hello","Shifa"]
print(type(a))
a=["Hello", 123, 'c', True, 6.0]
print(type(a))

# indexing
print(a[0])
print(a[-1])

# slicing
print(a[0:2])
print(a[::-1])
print(a[::2])

# Iteration using for loop
a=["John","Aaron","Joyo","Sara"]
for i in a:
    print(i)
print()
# Iteration using len and range
for i in range(len(a)):
    print(a[i])

# Iteration using while loop
a = ["John", "Aaron", "Joyo", "Sara"]
while a[0] == "John":
    print(a)
    break  # prevent infinite loop

i=0
while i<len(a):
    print(a[i])
    i+=1
# using short hand for loop
[print (i) for i in a]
