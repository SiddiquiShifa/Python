
for i in range (1,6,2):
    print(i)
    # Starts at 1 → next is 1+2 = 3 → then 3+2 = 5 → then 5+2 = 7 (but 7 is not less than 6, so loop stops)

for i in range(1,6):
    print("Hello world")

n=7
for i in range(1,11):
    print(n,"x",i,"=", n*i)

n=int(input("Enter a num :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# Characters of a string
for i in "Shifa":
 print(i)


# Loop through a list/array and print each element.

fruit_list=["apple","mango", 1, "Shifa", "Safiya"]
for i in fruit_list:
    print(i)

# pattern printing
rows=4
for i in range(1,rows+1) : # Outer loop: row number
    for j in range(1,i+1): # Inner loop: how many * to print
        print("*", end="") # Print * on the same line
    print() # Move to next line after each row

# Difference when end i="" 
name="Safa"
for i in name:
    print(i,end="")
print()
for j in name:
    print(j)

for k in name:
    for l in k:
        print(l,l+k)

rows=4
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(j,end="")
    print()

a = int(input("Enter number of rows: "))

for i in range(1, a + 1):                  # i = row number
    for j in range(1, i + 1):           
        print(j, end=" ")
    print()                                # move to next line


# Hacker rank problm
# Task
# The provided code stub reads an integer,i<n , from STDIN. For all non-negative integers , print .
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if i<n:
            print(i**2)