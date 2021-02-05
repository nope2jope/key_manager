from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# #Password Generator Project
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#
#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)
#
#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    app_key = API_entry.get()
    auth_other = AUTH_entry.get()

    if len(website) == 0 or len(auth_other) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"ERROR")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {app_key} | {auth_other}\n")
                website_entry.delete(0, END)
                app_key.delete(0, END)
                auth_other.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("m a n a g e  k e y s")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="blossom.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
API_label = Label(text="API Key:")
API_label.grid(row=2, column=0)
AUTH_label = Label(text="AUTH/Other:")
AUTH_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
API_entry = Entry(width=35)
API_entry.grid(row=2, column=1, columnspan=2)
AUTH_entry = Entry(width=35)
AUTH_entry.grid(row=3, column=1, columnspan=2)

# Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()