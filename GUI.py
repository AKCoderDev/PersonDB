from tkinter import *
import customtkinter
import sql
from tkinter import messagebox, filedialog
# import ttkbootstrap as tb
from datetime import datetime


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()


root.title('PersonDB')
root.geometry('800x500')
root.eval('tk::PlaceWindow . center')

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
    passport_entry.place_forget()
    theme_button.place_forget()

def show_main_from_settings():
    button_open.place(x=40, y=40)
    button_create.place(x=40, y=80)
    button_settings.place(x=40, y=120)
    button_show_about.place(x=40, y=160)
    button_exit.place(x=40, y=200)
    back_to_main_from_settings.place_forget()
    theme_button.place_forget()



# CREATE


def create_person():
    passport = passport_entry.get()
    photo = photo_entry.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    gender = gender_entry.get()
    phone_number = phone_number_entry.get()
    date_of_birthday = tb.DateEntry(root, bootstyle='danger')
    date_of_birthday.place(y=50, x=50)
    notes = notes_entry.get()

    if not passport or not photo or not firstname or not lastname or not gender or not phone_number or not date_of_birthday:
        messagebox.showerror('Bład', 'Wszystkie pola muszą być wypełnione.')
        return

# creation of input fields


def create():
    hide_main()
    passport_entry = customtkinter.CTkEntry(
        frame, placeholder_text="Passport ID")
    photo_entry = customtkinter.CTkEntry(frame, placeholder_text="link")
    firstname_entry = customtkinter.CTkEntry(
        frame, placeholder_text="firstname")
    lastname_entry = customtkinter.CTkEntry(frame, placeholder_text="lastname")
    gender_entry = customtkinter.CTkEntry(frame, placeholder_text="gender")
    phone_number_entry = customtkinter.CTkEntry(
        frame, placeholder_text="phone number")
    date_of_birthday_entry = customtkinter.CTkEntry(
        frame, placeholder_text="date of birthday")
    notes_entry = customtkinter.CTkEntry(frame, placeholder_text="Notes")
    passport_entry.place(x=460, y=40)
    photo_entry.place(x=460, y=80)
    firstname_entry.place(x=460, y=120)
    lastname_entry.place(x=460, y=160)
    gender_entry .place(x=460, y=200)
    phone_number_entry.place(x=460, y=240)
    date_of_birthday_entry.place(x=460, y=280)
    notes_entry.place(x=460, y=320)
    back_to_main_from_settings.place(x=40, y=350)

# SETTINGS


def settings():
    hide_main()
    theme_button.place(x=40, y=40)
    back_to_main_from_settings.place(x=40, y=350)


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
    # window_about.geometry('300x150')
    window_width = 300
    window_height = 150
    window_about.geometry(f"{window_width}x{window_height}")
    window_about.after(100, window_about.lift)
    screen_width = window_about.winfo_screenwidth()
    screen_height = window_about.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window_about.geometry(f"+{x}+{y}")
    label = customtkinter.CTkLabel(
        window_about, wraplength=250, text='PersonDB is an application for browsing databases of people. The application allows you to add new records, search for existing records and change personal data. Version 0.0.0.1')
    label.pack(padx=0.5, pady=40)

# EXIT


def close_app():
    root.destroy()


# ALL_BUTTONS
button_open = customtkinter.CTkButton(
    frame, text='Open', command=lambda: print('Działa'))
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
back_to_main_from_settings = customtkinter.CTkButton(
    frame, text='Back', command=show_main_from_settings)
back_to_main_from_create = customtkinter.CTkButton(
    frame, text='Back', command=show_main_from_create)


root.mainloop()
