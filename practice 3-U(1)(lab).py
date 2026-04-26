#PRACTICE 3 (PERFECT NUMBER)
n=int(input("ENTER N VALUE:"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("PERFECT NUMBER")
else:
    print("NOT A PERFET NUMBER")
 
