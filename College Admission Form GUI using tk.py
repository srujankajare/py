College Admission Form GUI using tkinter 

import tkinter as tk 
def submit(): 
    print("Name:", name_entry.get()) 
    print("Branch:", branch_entry.get()) 
    print("Favorite Game:", game_entry.get()) 
root = tk.Tk() 
root.title("College Admission Form") 
tk.Label(root, text="Name").grid(row=0) 
tk.Label(root, text="Branch").grid(row=1) 
tk.Label(root, text="Favorite Game").grid(row=2) 
name_entry = tk.Entry(root) 
branch_entry = tk.Entry(root) 
game_entry = tk.Entry(root) 
name_entry.grid(row=0, column=1) 
branch_entry.grid(row=1, column=1) 
game_entry.grid(row=2, column=1) 
tk.Button(root, text="Submit", command=submit).grid(row=3, column=1) 
root.mainloop() 