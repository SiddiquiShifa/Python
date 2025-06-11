i=0
while (i<3):
    print(i)
    i+=1

a=int(input("enter: "))
while (a<3):
    a=int(input("enter: "))
    print(a)

b=5
while (b>0): #write a condition it should be true ......logic...
    print(b)
    b-=1
else:
    print("Out of while loop")

#  Print Numbers from 1 to N
ip=int(input("Enter input :"))
while (ip<=3):
    print(ip)
    ip+=1

# Guess the Secret Number
secret_num = 7  # The number the user needs to guess
while True:
    guess = int(input("Guess the number: "))  # Prompt user for input
    if guess == secret_num:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop if the guess is correct
    else:
        print("Wrong guess, try again!")

# Multiplication Table
n=1
a=3
while n<=10:
    print(a*n)
    n+=1

n=1
a=int(input("Enter num : "))
while n<=10:
    print(a*n)
    n+=1

# While TRUE
while True:
    a=int(input("Enter num1: "))
    a2=int(input("Enter num2: "))
    sum=a+a2
    print(sum)

    # now this above will ask for input continuously
    # if we want that user may stop this program then:

    repeat=input('Do you wanna stop this loop :')
    if repeat=='yes' or repeat=="Yes":
        print("Stopped")
        break
        
    else:
        continue