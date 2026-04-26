class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name is:",self.name)
        print("AGE IS:",self.age)
p1=person("LOHI",18)
p1.display()
