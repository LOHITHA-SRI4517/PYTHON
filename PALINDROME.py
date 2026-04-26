#PALINDROME
n=int(input("Enter N Value:"))
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==n:
    print("Palindrome")
else:
    print("Not a Palindrome")
