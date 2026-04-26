#1
try:
    marks=45
    result=25/0
    print(result)
except ZeroDivisionError:
    print("A Number Cannot be Divide By Zero")


#2
try:
    list=[1,2,3,4]
    print(list[10])
except IndexError:
    print("This is Out of Index")

#3
try:
    f=open("haloooo","r")
except FileNotFoundError:
    print("File Is Not Found")
finally:
    print("Code Successfully executed")#finally block is executued even exception is there or not

#4
try:
    a=10
    b="Lohitha"
except TypeError:
    print("Number and String cant be added")
finally:
    print("CODE EXECUTION COMPLETED")

#5
try:
    f=open("studentregistration","r")
    print(f.readlines())
except FileNotFoundError:
    print("File Is Not Found")
finally:
    print("Code Successfully executed")

#6
try:
    a=[1,2,3,4]
    print(A)
except NameError:
    print("A is not Defined")
finally:
    print("Code is Successfully Executed")

#7
try:
    print(int("ab"))
except ValueError:
    print("String cant change to int")
finally:
    print("code is executed")

#7
try:
    a,b=map(int,int().s())
    print(a+b)
except AttributeError:
    print("Got Attribute Error Check Again")
finally:
    print("Code is executed successfully")
