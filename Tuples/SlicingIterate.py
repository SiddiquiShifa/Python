a="OnePlus","vivo","samsung","redmi","moto","nokia"
print(a[1:3])

# to print starting three values
print(a[:3])

# 2 to end
print(a[1:])

# to gap
print(a[::2])
print(a[1::2])
print(len(a))
print(a[1::4])

# reverse
print(a[::-1])

# iterate
for i in a:
    print(i)
print()
for i in range(len(a)):
    print(a[i])

# using while loop
i=0
while i<len(a):
    print(a[i])
    i+=1
    