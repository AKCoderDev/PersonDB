from tkinter import *
import tkinter as tk
import customtkinter
from customtkinter import CTk, CTkLabel
from data_base import Person,session
from sqlalchemy.orm import sessionmaker
from tkinter import messagebox, filedialog, ttk
from datetime import datetime
import re
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title('PersonDB')
#root.geometry('800x500')
#root.eval('tk::PlaceWindow . center')
window_width = 800
window_height = 560
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
x+=80
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.wm_minsize(window_width,window_height)

frame = customtkinter.CTkFrame(root, width=300, height=150, corner_radius=10)
frame.pack(pady=20, padx=20, fill='both', expand=True)

def hide_main():
    button_open.place_forget()
    button_create.place_forget()
    button_settings.place_forget()
    button_show_about.place_forget()
    button_exit.place_forget()

def show_main_from_create():
    button_open.place(x=40, y=40)
    button_create.place(x=40, y=80)
    button_settings.place(x=40, y=120)
    button_show_about.place(x=40, y=160)
    button_exit.place(x=40, y=200)
    passport_label.place_forget()
    passport_entry.place_forget()
    photo_label.place_forget()
    photo_entry.place_forget()
    firstname_label.place_forget()
    firstname_entry.place_forget()
    lastname_label.place_forget()
    lastname_entry.place_forget()
    gender_label.place_forget()
    gender_entry.place_forget()
    phone_number_label.place_forget()
    phone_number_entry.place_forget()
    date_of_birthday_label.place_forget()
    date_of_birthday_entry.place_forget()
    notes_label.place_forget()
    notes_entry.place_forget()
    enter_button.place_forget()
    back_to_main_from_create.place_forget()
    theme_button.place_forget()

def show_main_from_settings():
    button_open.place(x=40, y=40)
    button_create.place(x=40, y=80)
    button_settings.place(x=40, y=120)
    button_show_about.place(x=40, y=160)
    button_exit.place(x=40, y=200)
    back_to_main_from_settings.place_forget()
    theme_button.place_forget()

#OPEN
def setup_style():
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#f1f1f1", foreground="#333333")
    style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    style.map("Treeview", background=[("selected", "#347083")], foreground=[("selected", "white")])

def read_base():
    hide_main()
    setup_style()
    global tree
    back_to_main_from_open.place(x=40, y=470)
    tree = ttk.Treeview(root, columns=('Passport', 'Firstname', 'Lastname', 'Age','Gender','Phone number','Date of birthday','Notes'), show='headings')

    tree.heading('Passport', text='Passport')
    tree.heading('Firstname', text='Firstname')
    tree.heading('Lastname', text='Lastname')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')
    tree.heading('Phone number', text='Phone number')
    tree.heading('Notes', text='Notes')
    tree.heading('Date of birthday', text='Date of birthday')

    tree.column('Passport', anchor='center',width=90)
    tree.column('Firstname',anchor='center',width=90)
    tree.column('Lastname', anchor='center',width=90)
    tree.column('Age',anchor='center',width=30)
    tree.column('Gender',anchor='center',width=60)
    tree.column('Phone number',anchor='center',width=100)
    tree.column('Date of birthday',anchor='center',width=100)
    tree.column('Notes',anchor='center',width=30)

    tree.place(x=90, y= 60, width=825, height=500)

    tree.bind('<Double-1>', open_details_windows)

    people = session.query(Person).all()
    for person in people:
        tree.insert('', tk.END, values=(person.passport, person.firstname, person.lastname, person.age, person.gender, person.phone_number, person.date_of_birthday,person.notes))

def open_details_windows(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, 'values')

    details_window = customtkinter.CTkToplevel()
    details_window.title("Person Details")
    window_width = 600
    window_height = 400
    details_window.after(100, details_window.lift)
    screen_width = details_window.winfo_screenwidth()
    screen_height = details_window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    x+=25
    details_window.geometry(f"600x400+{x}+{y}")

    passport_label = CTkLabel(details_window, text=f"Passport: {values[0]}")
    passport_label.pack()

    firstname_label = CTkLabel(details_window, text=f"Firstname: {values[1]}")
    firstname_label.pack()

    lastname_label = CTkLabel(details_window, text=f"Lastname: {values[2]}")
    lastname_label.pack()

    age_label = CTkLabel(details_window, text=f"Age: {values[3]}")
    age_label.pack()
    
    gender_label = CTkLabel(details_window, text=f"Gender: {values[4]}")
    gender_label.pack()

    phone_number_label = CTkLabel(details_window, text=f"Phone number: {values[5]}")
    phone_number_label.pack()

    date_of_birthday_label = CTkLabel(details_window, text=f"Date of birthday: {values[6]}")
    date_of_birthday_label.pack()

    notes_label = CTkLabel(details_window, text=f"Notes: {values[7]}")
    notes_label.pack()

    image_path = 'C:/projects/photos/1.jpg'
    image = image.open(image_path)
    image = image.resize((200,200)), Image.ANTIALIAS
    photo = customtkinter.CtkImage(image)

    photo_label = customtkinter.CTkLabel(details_window, image=photo)
    photo_label.image = photo
    photo_label.pack()

def show_main_from_open():
    button_open.place(x=40, y=40)
    button_create.place(x=40, y=80)
    button_settings.place(x=40, y=120)
    button_show_about.place(x=40, y=160)
    button_exit.place(x=40, y=200)
    back_to_main_from_open.place_forget()
    tree.place_forget()

# CREATE
def clear_fields():
    passport_entry.delete(0,'end')
    photo_entry.delete(0,'end')
    firstname_entry.delete(0,'end')
    lastname_entry.delete(0,'end')
    gender_entry.delete(0,'end')
    phone_number_entry.delete(0,'end')
    date_of_birthday_entry.delete(0,'end')
    notes_entry.delete(0,'end')
def validate_phone_number(phone_number):
        pattern = re.compile(r'^\+?[0-9]{10,13}$')
        return pattern.match(phone_number) is not None
def save_data():
    passport = passport_entry.get().upper()
    photo = photo_entry.get()
    firstname = firstname_entry.get().capitalize()
    lastname = lastname_entry.get().capitalize()
    gender = gender_entry.get().capitalize()
    phone_number = phone_number_entry.get()
    date_of_birthday_str = date_of_birthday_entry.get()
    notes = notes_entry.get().capitalize()

    if not passport or not photo or not firstname or not lastname or not gender or not phone_number or not date_of_birthday_str:
        messagebox.showerror('Error', 'All fields must be filled out')
        return
    if not validate_phone_number(phone_number):
        messagebox.showerror('Error', "Phone number isn't correct")
        return
    try:
        date_of_birthday = datetime.strptime(date_of_birthday_str, '%d.%m.%Y').date()
    except ValueError:
        messagebox.showerror('Error', 'Incorrect date format. Use format: DD.MM.YYYY.')
        return

    new_person = Person(
        passport=passport,
        photo=photo,
        firstname=firstname,
        lastname=lastname,
        gender=gender,
        phone_number=phone_number,
        date_of_birthday=date_of_birthday,
        notes=notes,
    )

    new_person.age = new_person.calculate_age()

    session.add(new_person)
    session.commit()
    messagebox.showinfo("Sukces", "The person has been added successfully!")
    clear_fields()
    
# creation of input fields
def create():
    hide_main()
    passport_label.place(x=40, y=40)
    passport_entry.place(x=141, y=40)
    photo_label.place(x=40, y=80)
    photo_entry.place(x=141, y=80)
    firstname_label.place(x=40, y=120)
    firstname_entry.place(x=141, y=120)
    lastname_label.place(x=40, y=160)
    lastname_entry.place(x=141, y=160)
    gender_label.place(x=40, y=200)
    gender_entry .place(x=141, y=200)
    phone_number_label.place(x=40, y=240)
    phone_number_entry.place(x=141, y=240)
    date_of_birthday_label.place(x=40, y=280)
    date_of_birthday_entry.place(x=141, y=280)
    notes_label.place(x=40, y=320)
    notes_entry.place(x=141, y=320)
    enter_button.place(x=210, y=375)
    back_to_main_from_create.place(x=40, y=375)

# SETTINGS
def settings():
    hide_main()
    theme_button.place(x=40, y=40)
    back_to_main_from_settings.place(x=40, y=356)

mode = 'dark'

def change_theme():
    global mode
    if mode == 'dark':
        customtkinter.set_appearance_mode('light')
        mode = 'light'
    else:
        customtkinter.set_appearance_mode('dark')
        mode = 'dark'

# ABOUT
def show_about():
    window_about = customtkinter.CTkToplevel()
    window_about.title('About')
    window_about.geometry('300x200')
    window_width = 50
    window_height = 200
    window_about.after(100, window_about.lift)
    screen_width = window_about.winfo_screenwidth()
    screen_height = window_about.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    x+=25
    window_about.geometry(f"300x200+{x}+{y}")
    label = customtkinter.CTkLabel(
        window_about, wraplength=250, text='PersonDB\n'
        'Version 0.0.0.1\n'
        'Developer: Antek\n'
        'Contact: example@example.com\n'
        'Website: example.com\n'
        'License: example License\n'
        'Copyright: © 2024 MyCompany\n')
    label.pack(padx=0.5, pady=40)

# EXIT
def close_app():
    root.destroy()

# Input fields
passport_label = customtkinter.CTkLabel(frame, text="Passport ID:")
passport_entry = customtkinter.CTkEntry(
    frame, placeholder_text="Passport ID")
photo_label = customtkinter.CTkLabel(frame, text="Photo link:")
photo_entry = customtkinter.CTkEntry(frame, placeholder_text="link")
firstname_label = customtkinter.CTkLabel(frame, text="Firstname:")
firstname_entry = customtkinter.CTkEntry(
    frame, placeholder_text="firstname")
lastname_label = customtkinter.CTkLabel(frame, text="Lastname:")
lastname_entry = customtkinter.CTkEntry(frame, placeholder_text="lastname")
gender_label = customtkinter.CTkLabel(frame, text="Gender:")
gender_entry = customtkinter.CTkEntry(frame, placeholder_text="gender")
phone_number_label = customtkinter.CTkLabel(frame, text="Phone number:")
phone_number_entry = customtkinter.CTkEntry(
    frame, placeholder_text="phone number")
date_of_birthday_label = customtkinter.CTkLabel(
    frame, text="Date of birthday:")
date_of_birthday_entry = customtkinter.CTkEntry(
    frame, placeholder_text="Date of birthday")
notes_label = customtkinter.CTkLabel(frame, text="Notes:")
notes_entry = customtkinter.CTkEntry(frame, placeholder_text="Notes")

# ALL_BUTTONS
button_open = customtkinter.CTkButton(
    frame, text='Open', command=read_base)
button_open.place(x=40, y=40)
button_create = customtkinter.CTkButton(
    frame, text='Create', command=create)
button_create.place(x=40, y=80)
button_settings = customtkinter.CTkButton(
    frame, text='Settings', command=settings)
button_settings.place(x=40, y=120)
button_show_about = customtkinter.CTkButton(
    frame, text='About', command=show_about)
button_show_about.place(x=40, y=160)
button_exit = customtkinter.CTkButton(
    frame, text='Exit', command=close_app)
button_exit.place(x=40, y=200)
theme_button = customtkinter.CTkButton(
    frame, text='Change theme', command=change_theme)
enter_button = customtkinter.CTkButton(frame, text='Enter', command=save_data)
back_to_main_from_settings = customtkinter.CTkButton(
    frame, text='Back', command=show_main_from_settings)
back_to_main_from_create = customtkinter.CTkButton(
    frame, text='Back', command=show_main_from_create)
back_to_main_from_open = customtkinter.CTkButton(
    frame, text='Back', command=show_main_from_open)

root.mainloop()