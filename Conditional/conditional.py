a=80
if a>=35:
     print("Pass")

print("WELL")

# problems
# If the number is divisible by 2 (num % 2 == 0), it's even.
a=int(input("Enter a number : "))
if a%2==0:
     print("Its even")
else:
     print(f"Odd {a}")

# Area calc
print("Area Calculator")

print("Enter 1 to get area of square")
print ("Enter 2 to get area of circle")
print("Enter 3 to get area of triangle")
print("Enter 4 to get area of rectangle")

choice=(input("Enter no. of particular to get the area: "))


if choice=="1" or "one": #choice is not declared any thts why ots string
     side=float(input("Enter the length of square : "))
     print(f"Area of {choice} one is :", side**2)

elif choice==2 or choice=="two":
     side=float(input("Enter the radius : "))
     area=(3.14)*(side**2)
     print(area)

elif choice== 3 or choice=="three":
     base=float(input("Enter the base : "))
     base2=float(input("Enter the height : "))

     area=0.5*base*base2
     print(area)

elif choice==4 or choice=="four":
     side=float(input("Enter the length : "))
     side2=float(input("Enter the breadth : "))
     print(f"Area of {choice} one is :", side*side2)

else:
     print("Invalid input")

# letter is vowel?
a=str(input("Enter any letter \nTo check uts vowel :"))
if a in "a,e,o,i,u" or (a in "AEIOU"):
     print(f"Fala {a} is vowel")
else:
     print("Its not vowel")

num =int(input("Enter the number to check if its single digit or two digit"))
if 9<num <100:
    print("Its two digit")
elif num>100 and num<1000:
    print("Three digit")
else:
    print("Its Single")