import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    save = False
    if len(website_entry.get()) == 0 or len(website_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror("Invalid validation", "You need to fill your empty fields!")
    else:
        save = messagebox.askokcancel(website_entry.get(), f"These are the details entered: "
                                                    f"\nEmail: {email_entry.get()} "
                                                    f"\nPassword: {password_entry.get()} "
                                                    f"\nIs it okay to save?")

    if save == True:
        with open("data.txt", mode="a") as data:
            data.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Password manager")

# ---------------------------- Row 0 ------------------------------- #
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(103, 112, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- Row 1 ------------------------------- #
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

# ---------------------------- Row 2 ------------------------------- #
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# ---------------------------- Row 3 ------------------------------- #
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

generate_button = tkinter.Button(text="Generate Password", command=password_gen)
generate_button.grid(row=3, column=2, sticky="EW")

# ---------------------------- Row 4 ------------------------------- #
submit_button = tkinter.Button(text="Add", width=36, command=save_password)
submit_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()