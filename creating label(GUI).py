import tkinter as tk
root=tk.Tk()#SYNTAX
root.title("Simple GUI")
root.geometry("300x200")#SET OF STATEMENTS
label=tk.Label(root,text="Hello GUI")#CREATING LABEL
label.pack()#PLACING LABEL ON WINDOW
root.mainloop()
