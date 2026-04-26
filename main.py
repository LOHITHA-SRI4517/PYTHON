#READ MODE
f=open("example21.txt","r")
print(f.readlines())# to read multiple lines
f.close()

f=open("example21.txt","r")
print(f.read())# to read
f.close()


f=open("example21.txt","r")
print(f.readline())# to read single line
f.close()


f=open("example21.txt","r")
print(f.read(7))#to read 5 characters
f.close()
