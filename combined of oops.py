class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print("EMPLOYEES DO THE WORK")
class Manager(Employee):
    def work(self):
        print(self.name, "The Manager manages the team")
class Tester(Employee):
    def work(self):     #OVER_RIDING:SAME METHOD &SAME ATTRIBUTES
        print(self.name, "The tester tests the code")
def Employee_details(emp):
    emp.work()
M = Manager("girls:")
T = Tester("boys:")
Employee_details(M)
Employee_details(T)
