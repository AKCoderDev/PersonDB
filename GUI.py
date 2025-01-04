from tkinter import *
import tkinter as tk
import customtkinter
from customtkinter import CTkImage, CTkLabel
import customtkinter as CTk
from data_base import Person,session
from sqlalchemy.orm import sessionmaker
from tkinter import messagebox, filedialog, ttk
from datetime import datetime
import re
from PIL import Image, ImageTk
import io
from customtkinter import CTkLabel, CTkFont

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title('PersonDB')
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
    upload_button.place_forget()
    first_name_label.place_forget()
    first_name_entry.place_forget()
    last_name_label.place_forget()
    last_name_entry.place_forget()
    gender_label.place_forget()
    gender_entry.place_forget()
    phone_number_label.place_forget()
    phone_number_entry.place_forget()
    date_of_birth_label.place_forget()
    date_of_birth_entry.place_forget()
    notes_label.place_forget()
    notes_entry.place_forget()
    enter_button.place_forget()
    back_to_main_from_create.place_forget()
    theme_button.place_forget()
    remove_button.place_forget()
    upload_button.place_forget()
    remove_photo(create_upload_button=False)
    clear_fields()
    
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
    tree = ttk.Treeview(root, columns=('Passport', 'first_name', 'last_name', 'Age','Gender','Phone number','Date of birth','Notes'), show='headings')

    tree.heading('Passport', text='Passport')
    tree.heading('first_name', text='First name')
    tree.heading('last_name', text='Last name')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')
    tree.heading('Phone number', text='Phone number')
    tree.heading('Notes', text='Notes')
    tree.heading('Date of birth', text='Date of birth')

    tree.column('Passport', anchor='center',width=90)
    tree.column('first_name',anchor='center',width=90)
    tree.column('last_name', anchor='center',width=90)
    tree.column('Age',anchor='center',width=30)
    tree.column('Gender',anchor='center',width=60)
    tree.column('Phone number',anchor='center',width=100)
    tree.column('Date of birth',anchor='center',width=100)
    tree.column('Notes',anchor='center',width=30)

    tree.place(x=90, y= 60, width=825, height=500)

    tree.bind('<Double-1>', open_details_windows)

    people = session.query(Person).all()
    for person in people:
        tree.insert('', tk.END, values=(person.passport, person.first_name, person.last_name, person.age, person.gender, person.phone_number, person.date_of_birth,person.notes))

def open_details_windows(event):
    
    selected_item = tree.selection()
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
    
    font = CTkFont(size=20)

    passport_label = CTkLabel(details_window, text=f"Passport: {values[0]}", font=font)
    passport_label.place(x = 30, y = 20)
    
    first_name_label = CTkLabel(details_window, text=f"First name: {values[1]}", font=font)
    first_name_label.place(x = 30, y = 50)

    last_name_label = CTkLabel(details_window, text=f"Last name: {values[2]}", font=font)
    last_name_label.place(x = 30, y = 80)

    age_label = CTkLabel(details_window, text=f"Age: {values[3]}", font=font)
    age_label.place(x = 30, y = 110)
    
    gender_label = CTkLabel(details_window, text=f"Gender: {values[4]}", font=font)
    gender_label.place(x = 30, y = 140)

    phone_number_label = CTkLabel(details_window, text=f"Phone number: {values[5]}", font=font)
    phone_number_label.place(x = 30, y = 170)

    date_of_birth_label = CTkLabel(details_window, text=f"Date of birth: {values[6]}", font=font)
    date_of_birth_label.place(x = 30, y = 200)

    notes_label = CTkLabel(details_window, text=f"Notes: {values[7]}", font=font, wraplength=500,justify="left")
    notes_label.place(x = 30, y = 230)

    person = session.query(Person).filter_by(passport=values[0]).first()
    print(f"Type of person.photo: {type(person.photo)}")

    if Person:  #Check in base
        if Person.photo:  #Check picture
            print(f"Photo data length: {len(person.photo)} bytes")
            try:
                image = Image.open(io.BytesIO(person.photo))
                image = image.resize((150, 150))
                photo_image = ImageTk.PhotoImage(image)

                #image display
                photo_label = CTkLabel(details_window, image=photo_image, text = " ")
                photo_label.image = photo_image
                photo_label.place(x=390, y=20)
            except Exception as e:
                print(f"Error displaying photo: {e}")
        else:
            print("No photo available for this person.")
    else:
        print("Person not found in the database.")

#Photo
photo_data = None
def upload_photo():
    global photo_data
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.bmp;*.png")])
    if file_path:
        print(f"Selected file: {file_path}")
        with open(file_path, 'rb')as file:
            photo_data = file.read()
        upload_button.configure(text="Photo uploaded", state = DISABLED)
        remove_button.place(x=320, y=100)

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
    upload_button.configure(text="Upload Photo", state=tk.NORMAL)
    first_name_entry.delete(0,'end')
    last_name_entry.delete(0,'end')
    gender_entry.delete(0,'end')
    phone_number_entry.delete(0,'end')
    date_of_birth_entry.delete(0,'end')
    notes_entry.delete(0,'end')
def validate_phone_number(phone_number):
        pattern = re.compile(r'^\+?[0-9]{10,13}$')
        return pattern.match(phone_number) is not None

def validate_gender(gender):
    if (re.search(r"F",gender) or
        re.search(r"M",gender) or
        re.search(r"Female",gender) or
        re.search(r"Male",gender)):
        return True
    return False

def remove_photo(create_upload_button=True):
    global photo_data
    photo_data = None
    photo_label.configure(image=None)
    photo_label.image = None
    if create_upload_button:
        upload_button.configure(state = "normal")
        remove_button.place_forget()
        upload_button.place(x=160, y=100)

def save_data():
    passport = passport_entry.get().upper()
    #photo = upload_button.get()
    first_name = first_name_entry.get().capitalize()
    last_name = last_name_entry.get().capitalize()
    gender = gender_entry.get().capitalize()
    phone_number = phone_number_entry.get()
    date_of_birth_str = date_of_birth_entry.get()
    notes = notes_entry.get().capitalize()

    if not passport  or not first_name or not last_name or not gender or not phone_number or not date_of_birth_str:
        messagebox.showerror('Error', 'All fields must be filled out')
        return
    if not validate_phone_number(phone_number):
        messagebox.showerror('Error', "Phone number isn't correct")
        return
    if not validate_gender(gender):
        messagebox.showerror('Error','Gender is not correct')
        return
    try:
        date_of_birth = datetime.strptime(date_of_birth_str, '%d.%m.%Y').date()
    except ValueError:
        messagebox.showerror('Error', 'Incorrect date format. Use format: DD.MM.YYYY.')
        return

    new_person = Person(
        passport=passport,
        photo=photo_data,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
        notes=notes,
    )

    new_person.age = new_person.calculate_age()

    session.add(new_person)
    session.commit()
    messagebox.showinfo("Success", "The person has been added successfully!")
    remove_button.place_forget()
    clear_fields()
    
# creation of input fields
def create():
    hide_main()
    passport_label.place(x=40, y=40)
    passport_entry.place(x=141, y=40)
    photo_label.place(x=40, y=80)
    upload_button.place(x=160, y=100)
    first_name_label.place(x=40, y=120)
    first_name_entry.place(x=141, y=120)
    last_name_label.place(x=40, y=160)
    last_name_entry.place(x=141, y=160)
    gender_label.place(x=40, y=200)
    gender_entry .place(x=141, y=200)
    phone_number_label.place(x=40, y=240)
    phone_number_entry.place(x=141, y=240)
    date_of_birth_label.place(x=40, y=280)
    date_of_birth_entry.place(x=141, y=280)
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
        'Version 0.3\n'
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
photo_label = customtkinter.CTkLabel(frame, text="Photo:")
first_name_label = customtkinter.CTkLabel(frame, text="First name:")
first_name_entry = customtkinter.CTkEntry(
    frame, placeholder_text="First name")
last_name_label = customtkinter.CTkLabel(frame, text="Last name:")
last_name_entry = customtkinter.CTkEntry(frame, placeholder_text="Last name")
gender_label = customtkinter.CTkLabel(frame, text="Gender:")
gender_entry = customtkinter.CTkEntry(frame, placeholder_text="Gender")
phone_number_label = customtkinter.CTkLabel(frame, text="Phone number:")
phone_number_entry = customtkinter.CTkEntry(
    frame, placeholder_text="Phone number")
date_of_birth_label = customtkinter.CTkLabel(
    frame, text="Date of birth:")
date_of_birth_entry = customtkinter.CTkEntry(
    frame, placeholder_text="Date of birth")
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
upload_button = customtkinter.CTkButton(root, text="Upload Photo", command=upload_photo)
remove_button = customtkinter.CTkButton(root, text="Delete", command=remove_photo)

root.mainloop()