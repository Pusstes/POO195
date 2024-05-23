import Backend as bk
from Backend import *
import tkinter as tk
from tkinter import *

# Main window
root = tk.Tk()
root.title("TypeError")
root.geometry("800x400")

# Label
label = tk.Label(root, text="Ingresa un número, si sale tu nombre eres el ganador", font=("Arial", 20))
label.pack(pady=10)

# Entrada
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(pady=10) 

# Instancia de Backend
backend = bk.backend()

# Función para manejar el evento del botón  
def evento():
    entero = entry.get()
    try:
        resultado = backend.CadenaCaracter(entero)
        label1.config(text=resultado)
    except ValueError as e:
        label1.config(text=str(e)+".")
    except TypeError as e:
        label1.config(text=str(e))

# Boton
button1 = tk.Button(root, text="Verificar",  command=evento, font=("Arial", 20))
button1.pack(pady=10)

#label
label1 = tk.Label(root, text="", font=("Arial", 20))
label1.pack(pady=10)

# Run 
root.mainloop()
