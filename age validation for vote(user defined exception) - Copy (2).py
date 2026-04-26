#AGE VALIDATION FOR VOTE
#1st Method
class AgeIsSmallToVote(Exception):
    """Raised when age is small to vote"""
    pass
class AgeIsEligibleToVote(Exception):
    """Raised when age is eligible to vote"""
    pass
while True:
    try:
        age=int(input("Enter Age:"))
        if age<18:
                raise AgeIsSmallToVote
        elif age>=18:
            raise AgeIsEligibleToVote
        break
    except AgeIsSmallToVote:
        print("Person is not eligible to Vote")
    except AgeIsEligibleToVote:
        print("Person is eligible to vote")
        print()
    
#2nd Method
class AgeIsSmallToVote(Exception):
    pass

while True:
    try:
        age = int(input("Enter Age: "))
        
        if age < 18:
            raise AgeIsSmallToVote
        
        print("Person is eligible to vote")
        break

    except AgeIsSmallToVote:
        print("Person is not eligible to vote")
