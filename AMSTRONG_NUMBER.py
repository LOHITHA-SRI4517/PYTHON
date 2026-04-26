#ARMSTRONG NUMBER
n=int(input("Enter a Number:"))
temp=n
sum=0
number=len(str(n))
while temp>0:
    digit=temp%10
    sum=sum+(digit**number)
    temp=temp//10
if sum==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
