''' password generator gui using tkinter '''
import random
import json
import tkinter as tk
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    ''' get random password from keyboard_characters list '''
    keyboard_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '{', '|', '}', '~'
    ]
    password = []
    for _ in range(10):
        password.append(random.choice(keyboard_characters))

    random.shuffle(password)
    password_str = ''.join(password)
    pyperclip.copy(password_str)
    pass_input.delete(0, 'end')
    pass_input.insert(0, password_str)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_passwords():
    ''' take inputs from gui and save to file'''
    web = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        web: {
            "email": email,
            "password": password
        }}

    # check if website, email or password are empty
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            "One of the required fields is empty.\n Please fill in all fields."
            )
    else:
        try:
            with open("day29/data.json", 'r') as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("day29/data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4) #saves new data
        else:
            with open("day29/data.json", 'w') as data_file:
                # save updated data to file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, "end")
            pass_input.delete(0, "end")

# ---------------------------- SEARCH ------------------------------- #
def search():
    web = website_input.get()
    options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

    # check if website is empty
    if len(web) == 0:
        messagebox.showinfo(
            "Website name required.\n Please fill in."
            )
    else:
        try:
            with open("day29/data.json", 'r') as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(
            "No data file found. Have you saved any passwords yet?"
            )
            return
        else:
            # try block is overkill so used if/else below instead
            #
            # try:
            #     website_data = data[web]
            # except KeyError:
            #     messagebox.showerror(title="Error",
            #             message=f"No password found for {web}")
            # else:
            #     messagebox.showinfo(title='Found Password',
            #         message=f'The website {web} password is\n {website_data["password"]}')
            if web in data:
                email = data[web]["email"]
                password = data[web]["password"]
                messagebox.showinfo(title='Found Password',
                     message=f'The website {web} email is\n {email} and password is {password}')
            else:
                messagebox.showinfo(title='No Password Found',
                    message=f'No details for {web} exist')
        finally:
            website_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)

# set up the background image
canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
label_web = tk.Label(text="Website:")
label_web.grid(column=0, row=1)
label_email = tk.Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_pass = tk.Label(text="Password:")
label_pass.grid(column=0, row=3)

# entries
website_input = tk.Entry(width=21)
website_input.grid(column=1, row=1, sticky="ew")
website_input.focus()
email_input = tk.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew")
# prepopulate email
email_input.insert(0, "des.barrett.sub@gmail.com")
pass_input = tk.Entry(width=21)
pass_input.grid(column=1, row=3, sticky="ew")

# buttons
gen_pass_btn = tk.Button(text="Generate Password", command=generate_password,
                   bg="white")
gen_pass_btn.grid(column=2, row=3, sticky="ew")

add_btn = tk.Button(text="Add", width=44, bg="white", command=add_to_passwords)
add_btn.grid(column=1, row=4,sticky="ew",columnspan=3)

search_btn = tk.Button(text="Search", command=search,
                   bg="white")
search_btn.grid(column=2, row=1, sticky="ew")


window.mainloop()
