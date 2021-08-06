import json
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

# ---------------------------- SEARCH BY EMAIL ------------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file_data:
            search_data = json.load(file_data)
            if search_data[website_entry.get().title()]:
                messagebox.showinfo(website, f"Email: {search_data[website]['email']}\n"
                                                         f"Password: {search_data[website]['password']}")
    except FileNotFoundError:
        messagebox.showerror("File not found!", "The file doesn't exist")
    except KeyError:
        messagebox.showerror("Website not found", f"The website {website} doesn't exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    new_data = {
        website_entry.get().title(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(website_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror("Invalid validation", "You need to fill your empty fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.minsize(520, 400)
window.config(padx=50, pady=50, bg="#515E63")
window.title("Password manager")
window.iconbitmap("logo.ico")


# ---------------------------- Row 0 ------------------------------- #
canvas = tkinter.Canvas(width=200, height=200, bg="#515E63", highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(103, 112, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- Row 1 ------------------------------- #
website_label = tkinter.Label(text="Website:", bg="#515E63", fg="#C9D8B6", font=("Arial", 12))
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=30, bg="#F1ECC3")
website_entry.grid(row=1, column=1, sticky="W")

search_btn = tkinter.Button(text="Search", width=20, command=search_password, bg="#F1ECC3")
search_btn.grid(row=1, column=2, sticky="EW")

# ---------------------------- Row 2 ------------------------------- #
email_label = tkinter.Label(text="Email/Username:", bg="#515E63", fg="#C9D8B6", font=("Arial", 12))
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=35, bg="#F1ECC3")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# ---------------------------- Row 3 ------------------------------- #
password_label = tkinter.Label(text="Password:", bg="#515E63", fg="#C9D8B6", font=("Arial", 12))
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=30, bg="#F1ECC3")
password_entry.grid(row=3, column=1, sticky="W")

generate_button = tkinter.Button(text="Generate Password", command=password_gen, bg="#F1ECC3")
generate_button.grid(row=3, column=2, sticky="EW")

# ---------------------------- Row 4 ------------------------------- #
submit_button = tkinter.Button(text="Add", width=36, command=save_password, bg="#F1ECC3")
submit_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()