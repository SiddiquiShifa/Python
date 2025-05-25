a="Hello World"
print(len(a)) #counts the space as well

# Count
print(a.count('o'))

# upper
print(a.upper())

# lower
print(a.lower())
print(a.islower())

# index
print(a.index("o"))

# capitalize first letter is captialize
print(a.capitalize())

# find a letter returns index
print(a.find('W'))

# format
name="John Doe"
a="My name is {}"
print(a.format(name))
print(f"Hello------{name}")
print(name.center(30,'*'))

# name1="Sara"
# age=input("Enter age Sara: ")
# a1="My Name is {} and age is {}"
# print(a1.format(name1,age))

# center method
b="Hey"
print(b.center(50,'*')) #space is added


# converts upper into lowert, lower into upper
print(b.casefold())

# is it consists alphabets or alphanum

a='hello'
print(type(a))
b="123"
c="Hello1233@"
d="Hey23"
e="shifa 123"
print(a,a.isalnum())
if a.isalnum()==True:
    print("Yes, its")

print(b.isalnum())
print(e, "---",e.isalnum())

# returns true is its alphabet
print(a,a.isalpha())
print(b,b.isalpha())

# returns true if its decimal
print(a,a.isalpha())
print(b.isalpha())
a="1.2"
c="123" #decimal category
print(a,a.isdecimal())
print(c,c.isdecimal())

# inside strin if its digits
a="shifa1"
b="shifa"
c="123"
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

# inside string is it numeric
print(b.isnumeric())
print(c.isnumeric())

# checks if string is lowercase or not
print(a,a.islower())
print(c,c.islower())
a="HELLO"
print(a,a.islower())

# such that can see for istitle also a method

a="Harry potter"
print(a.endswith('r'))

print(a.startswith('h'))
# can also define range 
print(a.startswith('p',6))

# swap case
print(a,"---",a.swapcase())

# remove spaces
b="         harry "
print(b.strip())
c=" *harry   _     "
print(c.strip("*, ")) # the mentioned symbole were striped off (removed).

a="Hello . seprate . this one . string "
print (a.split('.'))

# left alignment of string
a="Harry Potter"
x=a.ljust(20,"-")
print(x,"Leaving space of 20, also u may add any symbol")

# right alignment
a="Shifa"
b="Siddiqui"
print(a.rjust(10,"-"),b.rjust(10))

# to replace specific value in a string
a="my name is john"
print(a)
print(a.replace("john","Shifa"),a.rjust(50,'-'))
print()
# if u want to know th index of a word... it will show the index of first letter of word u searching for
a="firs index of word Sara ,The index of S would be shown"
print(a.rindex("Sara"))
print("index start with zero")
print(a.rindex('f'))
print("yeh poori string ke andar last baar 'f' character jahan dikhega, uska index batayega.")

# rfind
a="Harry potter"
print(a.rfind('H'),"---rfind     rindex---",a.rindex('H'))
print("if not found in rfind returns: ", a.rfind("Sara"))
print()
# print("if not found in rindex returns: ", a.rindex("Sara")) #error

# u can find any word in given index range such as:
a="bibidy bobdy boo"
print(a.rfind('b',6,13))

