#SPY NUMBER
n=int(input("ENTER A NUMBER:"))
sum_digits=0
product_digits=1
temp=n
while temp>0:
    digit=temp%10
    sum_digits+=digit
    product_digits*=digit
    temp=temp/10
if sum_digits==product_digits:
        print("IT IS A SPY NUMBER.")
else:
        print("NOT A SPY NUMBER.")
