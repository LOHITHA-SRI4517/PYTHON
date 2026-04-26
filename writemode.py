#WRITE MODE
f=open("example21.txt","w")
f.write("MY NAME IS LOHITHA")# to write 
f.close()

#writelines
f = open("example21.txt","w")
f.write("MY NAME IS LOHITHA\n")
f.write("I AM A STUDENT\n")
f.write("I LIKE PYTHON\n")
f.close()

#other method for writelines
f = open("example21.txt", "w")
lines = [                       
    "MY NAME IS LOHITHA\n",
    "I AM A STUDENT\n",
    "I LIKE PYTHON\n"
]
f.writelines(lines)#to write multiple lines
f.close()
