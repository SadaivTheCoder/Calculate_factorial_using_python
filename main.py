# Write a program to calculate the factorial of number n:->
def facto(n):
    if(n==0):
        return 1
    else:
        return n*facto(n-1)
n = int(input("Enter a number:-> "))
print(facto(n))
