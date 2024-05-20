from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()


root.title('SQL_base')
root.geometry('800x500')
root.eval('tk::PlaceWindow . center')

frame = customtkinter.CTkFrame(root, width=300, height=150, corner_radius=10)
frame.pack(pady=20, padx=20, fill='both', expand=True)

def hide_main():
    button.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    

def show_main():
    button.place(x=40, y=40)
    button2.place(x=40, y=80)
    button3.place(x=40, y=120)
    button4.place(x=40, y=160)
    button5.place(x=40, y=200)
    back_to_main.place_forget()

def settings_buttons():
    hide_main()
    theme_button.place(x=40, y=40)
    back_to_main.place(x=40, y=350)
    

def settings():
    settings_buttons()

mode = 'dark'

def change_theme():
    global mode
    if mode == 'dark':
        customtkinter.set_appearance_mode('light')
        mode = 'light'
    else:
        customtkinter.set_appearance_mode('dark')
        mode = 'dark'


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


def close_app():
    root.destroy()


button = customtkinter.CTkButton(
    frame, text='Open', command=lambda: print('Działa'))
button.place(x=40, y=40)
button2 = customtkinter.CTkButton(
    frame, text='Create', command=lambda: print('Działa'))
button2.place(x=40, y=80)
button3 = customtkinter.CTkButton(
    frame, text='Settings', command=settings)
button3.place(x=40, y=120)
button4 = customtkinter.CTkButton(
    frame, text='About', command=show_about)
button4.place(x=40, y=160)
button5 = customtkinter.CTkButton(
    frame, text='Exit', command=close_app)
button5.place(x=40, y=200)
theme_button = customtkinter.CTkButton(
    frame, text='Change theme', command=change_theme)
back_to_main = customtkinter.CTkButton(
    frame, text='Back', command=show_main)




root.mainloop()
