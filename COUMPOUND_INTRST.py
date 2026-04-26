#COUMPOUND INTREST
p=float(input("ENTER PRICIPAL AMOUNT:"))
t=float(input("Enter Time:"))
r=float(input("ENTER RATE OF INTRST:"))
amount=p*(1+r/100)**t
ci=amount-p
print("Total Amount:",amount)
print("Compound Intrest:",ci)
