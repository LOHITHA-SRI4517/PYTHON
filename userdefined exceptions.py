#USER DEFINED EXCEPTIONS
class ValueTooSmallError(Exception):
    """Raised when input is tooo small"""
    pass
class ValueTooLargeError(Exception):
    """Raised when input is tooo large"""
    pass
number=10
while True:
    try:
        inum=int(input("Enter a number:"))
        if inum<number:
            raise ValueTooSmallError
        elif inum>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This Value is too small,try again!")
    except ValueTooLargeError:
        print("This Value is too large,try again!")
        print()
print("YEAH!You Have Guessed The Number")
