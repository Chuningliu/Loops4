#  Write a program to find the product of the digits of a number accepted from the user.


n=int(input("Enter the number:"))
product=1
while n>0:
    n=n%10
    product=product*n
    n=n//10
    print("Product of digit=",product)
