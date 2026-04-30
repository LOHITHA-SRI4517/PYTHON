import tkinter as tk
def login():
    user=entry_user.get()
    pwd=entry_pass.get()
    print("Username:",user)
    print("password:",pwd)
root=tk.Tk()

tk.Label(root,text="username").pack()
entry_user=tk.Entry(root)
entry_user.pack()

tk.Label(root,text="password:").pack()
entry_pass=tk.Entry(root,show="*")
entry_pass.pack()

tk.Button(root,text="login",command=login).pack()
root.mainloop()
