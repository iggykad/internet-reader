import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import ttk

root = tk.Tk()
root.title("Menu")
root.geometry("350x350")

menuFrame = tk.Frame(root)
menuFrame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

itemFrame = tk.Frame(root)
itemFrame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

def clear(object):
    slaves = object.pack_slaves()
    for x in slaves:
        x.destroy()

def login_page():
    clear(itemFrame)
    
    def validate():
        userid = username_entry.get()
        password = pass_entry.get()
        if userid == "sys" and password == "123":
            messagebox.showinfo("","Welcome, logging you in...")
            main_page() 
        else:
            messagebox.showerror("","Invalid user/password.")

    username_label = tk.Label(itemFrame, text="Username") 
    username_label.pack()

    username_entry = tk.Entry(itemFrame) 
    username_entry.pack()

    pass_label = tk.Label(itemFrame, text="Password")
    pass_label.pack()

    pass_entry = tk.Entry(itemFrame, show="*") 
    pass_entry.pack()

    button = tk.Button(itemFrame, text="Login", command=validate) 
    button.pack()

def main_page():
    clear(itemFrame)
    tk.Label(itemFrame, text="Welcome to the program!").pack()

def about_page():
    clear(itemFrame)
    tk.Label(itemFrame, text="2025 I.K.").pack()


tk.Button(menuFrame, text="Login", command=login_page).pack(fill="y", pady=5)
tk.Button(menuFrame, text="About", command=about_page).pack(fill="y", pady=5)


login_page()

root.mainloop()