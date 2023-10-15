import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

global_currency = 0

def while_input(event):
    if event.keysym == "Return":
        user_input = entry.get()  
        try:
            global global_currency
            global_currency = float(user_input)
            label_result.config(text="Currency (in INR) set to: {:.2f}".format(global_currency))
            entry.config(state=tk.DISABLED)
            show_reset_button() 
        except ValueError:
            if user_input.lower() == "chimz":
                easter_egg()
            else:
                label_result.config(text="Invalid input. Please enter a number.")

def show_reset_button():
    button4.place(relx=0.4475, rely=0.8)

def bitcoin():
    global global_currencyB
    result = global_currency * 0.00000043
    label_result.config(text="Bitcoins: {:.8f}".format(result))

def ethereum():
    global global_currency
    result = global_currency * 0.0000074
    label_result.config(text="Ethereum: {:.8f}".format(result))

def dogecoin():
    global global_currency
    result = global_currency * 0.20
    label_result.config(text="DogeCoins: {:.2f}".format(result))

def reset():
    global global_currency
    global_currency = 0
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    label_result.config(text="Currency (in INR) set to: 0.00")
    button4.place_forget()

def easter_egg():
    pil_image = Image.open("images/gufee.png")
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = tk.Label(window, image=tk_image)
    image_label.place(relx=0.5, rely=0.373, anchor=tk.CENTER)
    label.image = image_label
    label.pack()


window = tk.Tk()
window.title("Crypto Converter")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f"{screen_width}x{screen_height}")
window.configure(bg="#3f68d1")

entry = tk.Entry(window, width=40, font=("Atari Classic", 20), bg="#FAEBD7")
entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER) 
entry.bind("<Key>", while_input) 

button1 = tk.Button(window, text="BITCOIN", command=bitcoin, width=20, height=3, font=("Atari Classic", 10), bg="#FAEBD7")
button1.place(relx=0.3, rely=0.6, anchor=tk.CENTER) 

button2 = tk.Button(window, text="ETHEREUM", command=ethereum, width=20, height=3, font=("Atari Classic", 10), bg="#FAEBD7")
button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  

button3 = tk.Button(window, text="DOGECOIN", command=dogecoin, width=20, height=3, font=("Atari Classic", 10), bg="#FAEBD7")
button3.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

button4 = tk.Button(window, text="Reset", command=reset, width=15, height=2, font=("Atari Classic", 10), bg="#FAEBD7")
button4.place_forget()

label_result = tk.Label(window, text="", font=("Atari Classic", 15), width=75, height=3, bg="#3f68d1", fg="#FAEBD7")
label_result.place(relx=0.5, rely=0.7, anchor=tk.CENTER) 

pil_image = Image.open("images/image.png")
tk_image = ImageTk.PhotoImage(pil_image)
image_label = tk.Label(window, image=tk_image)
image_label.place(relx=0.5, rely=0.175, anchor=tk.CENTER)

window.mainloop()
