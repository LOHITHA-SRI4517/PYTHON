#PRACTICE 2 (PERFECT ROOT CHECK)
import math
n=int(input("ENTER N VALUE:"))
root=int(math.sqrt(n))
if root*root==n:
    print("Perfect Square")
else:
    print("Not Perfect Square")
