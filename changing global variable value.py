#CHANGE GLOBAL VARIABLE VALUE
x=100
def change():
    global x
    x=45
    print("GLOBAL VARIABLE IS:",x)
change()
