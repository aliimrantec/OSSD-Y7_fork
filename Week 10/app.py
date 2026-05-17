import tkinter as tk
from tkinter import messagebox

def read_file():
    try:
        file = open("user.txt", "r")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        return []

def write_file():
    file = open("user.txt", "a")
    file.write(entery.get() + "," + pas_entry.get() + "\n")
    file.close()

def login():
    if entery.get() == "" or pas_entry.get() == "":
        messagebox.showerror("Login Failed", "Fields khali nahi chor sakte! Pehle data enter karein.")
        return

    data_lines = read_file()
    user_found = False
    
    for i in data_lines:
        n, pas = i.strip().split(",")
        if entery.get() == n:
            user_found = True
            if pas_entry.get() == pas:
                messagebox.showinfo("Login", "Login successful")
                return
            else:
                messagebox.showerror("Login Failed", "Incorrect password")
                return

    if not user_found:
        messagebox.showerror("Login Failed", "Register first")

def signup():
    if entery.get() == "" or pas_entry.get() == "":
        messagebox.showerror("Error", "Fields khali nahi chor sakte!")
        return

    data_lines = read_file()
    for i in data_lines:
        n, _ = i.strip().split(",")
        if entery.get() == n:
            messagebox.showerror("Error", "Yeh username pehle se mojud hai!")
            return

    write_file()
    messagebox.showinfo("Signup", "Signup successful")
    entery.delete(0, tk.END)
    pas_entry.delete(0, tk.END)

def main():
    pass

root = tk.Tk()
root.title("Login System")   
root.geometry("400x440")
root.configure(bg="white")

main_name = tk.Label(
    root,
    text="Welcome to the Login System",
    font=("Comic Sans MS", 18, "bold"),
    bg="white",
    fg="black",
)
main_name.pack(pady=20)

login_frame = tk.Frame(root, bg="white")
login_frame.pack()

name_l = tk.Label(login_frame, text="Username :", bg="white", font=("Times New Roman", 12, "bold"))
name_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entery = tk.Entry(login_frame, bg="LIGHTBLUE", font=("Times New Roman", 12))
entery.grid(row=0, column=1, padx=10, pady=10)

pas_l = tk.Label(login_frame, text="Password :", bg="white", font=("Times New Roman", 12, "bold"))
pas_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")

pas_entry = tk.Entry(login_frame, show="*", bg="LIGHTBLUE", font=("Times New Roman", 12))
pas_entry.grid(row=1, column=1, padx=10, pady=10)

button_frame = tk.Frame(login_frame, bg="white")
button_frame.grid(row=2, column=0, columnspan=2, pady=20)

login_botten = tk.Button(button_frame, text="Login", bg='lightblue', width=10, command=login)
login_botten.pack(side="left", padx=10)

signup_botten = tk.Button(button_frame, text="Signup", bg="lightblue", width=10, command=signup)
signup_botten.pack(side="left", padx=10)

root.mainloop()