import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


root = tk.Tk()
root.title("Menu")
root.minsize(640, 360)
root.resizable(1280, 720)

menuFrame = tk.Frame(root)
menuFrame.pack(side="left", fill="both", padx=10, pady=10)

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

    text_widget = tk.Text(itemFrame, wrap='word')
    text_widget.pack(expand=True, fill='both')

    def response():
        print(page.text.prettify)
        if not response:
            raise Exception(f"Error {response.status_code}. Could not pull data.")
        

    get_news = tk.Button(menuFrame, text="Get HackerNews posts", 
                         command=lambda: text_widget.insert('end', page.text))
    get_news.pack()


def about_page():
    clear(itemFrame)
    tk.Label(itemFrame, text="2025 I.K.").pack()

tk.Button(menuFrame, text="Login", command=login_page).pack(fill="y", pady=5)
tk.Button(menuFrame, text="About", command=about_page).pack(fill="y", pady=5)



login_page() #runs on startup everytime

root.mainloop()