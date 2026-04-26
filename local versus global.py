#LOCAL V/S GLOBAL VARIABLE
x=100
def display():
    x=45
    print("LOCAL VARIABLE IS:",x)
display()
print("GLOBAL VARIABLE IS:",x)
