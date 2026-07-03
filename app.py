import tkinter as tk
import subprocess

def abrir_artesanos():
    subprocess.Popen(["python", "artesanos.py"])

def abrir_productos():
    subprocess.Popen(["python", "productos.py"])

def abrir_categorias():
    subprocess.Popen(["python", "categorias.py"])

ventana = tk.Tk()
ventana.title("Directorio Digital de Artesanos Mazahuas")
ventana.geometry("700x400")
ventana.config(bg="lightblue")

tk.Label(
    ventana,
    text="Sistema de Información para la Difusión de Artesanos Mazahuas",
    font=("Arial",16,"bold"),
    bg="lightblue"
).pack(pady=20)

tk.Button(
    ventana,
    text="Artesanos",
    width=25,
    command=abrir_artesanos
).pack(pady=10)

tk.Button(
    ventana,
    text="Productos",
    width=25,
    command=abrir_productos
).pack(pady=10)

tk.Button(
    ventana,
    text="Categorías",
    width=25,
    command=abrir_categorias
).pack(pady=10)

tk.Button(
    ventana,
    text="Salir",
    width=25,
    command=ventana.destroy
).pack(pady=20)

ventana.mainloop()