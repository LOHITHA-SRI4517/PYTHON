#program to read 2 values through keyboard in single line with , as operartor
a, b = input("Enter two values separated by comma: ").split(",")

a = int(a)
b = int(b)

print("Sum:", a + b)
