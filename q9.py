# Write a program to display all even numbers that fall between two numbers 
# (exclusive both numbers) entered by the user.


n=int(input("Enter the number"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1
