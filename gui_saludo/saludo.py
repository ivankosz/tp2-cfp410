import tkinter as tk
from tkinter import Tk, ttk
from turtle import textinput

ANCHO = 400
ALTO = 500

app = tk.Tk()
app.title("Saludo TKinter")
app.config(width=ANCHO, height=ALTO)

text1= ttk.Label(text="Escriba su nombre")
text1.place(x=20, y=20)

text_input = ttk.Entry()
text_input.place(x=160, y=20)

str_saludo = tk.StringVar()
ttk.Label()

text_saludo = ttk.Label(app, textvariable= str_saludo)
text_saludo.place(x=20, y=110)

def saludo():
    if len(text_input.get()):
        str_saludo.set(f"Hola {text_input.get()}")
    else:
        str_saludo.set(f"Hola amigazo!")

btn_saludo =ttk.Button(text="Saludame", command = saludo)
btn_saludo.place(x=20, y=70)

app.mainloop()

