class numdisplay:
    def __init__(self):
        self.x=100#INSTANCE VARIABlE        #can access outside of method
    def display(self):
        y=30#self varibale
        print("INSTANCE VARIABLE IS:",self.x)
        print("NORMAL VARAIBALE:",y)
n1=numdisplay()
n1.display()
print("INSTANT VARIABLE IS:",n1.x)
print(y)
