import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# ==========================
# CONFIGURACIÓN DE LA BD
# ==========================
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "directorio_artesanos"   # Cambia por tu base de datos
# ==========================
# CONEXIÓN
# ==========================
def conectar():
    try:
        conexion = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar:\n{e}")
        return None
# ==========================
# PROBAR CONEXIÓN
# ==========================
def probar_conexion():
    conexion = conectar()
    if conexion:
        messagebox.showinfo("Conexión", "Conexión exitosa con MySQL")
        conexion.close()
def insertar():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = """
        INSERT INTO artesanos(id_artesano,nombre,apellido,telefono,email,direccion,municipio,descripcion,pagina_web,redes_sociales )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        valores = (
            txt_id.get(),
            txt_nombre.get(),
            txt_apellido.get(),
            txt_telefono.get(),
            txt_email.get(),
            txt_direccion.get(),
            txt_municipio.get(),
            txt_descripcion.get(),
            txt_pagina_web.get(),
            txt_redes_sociales.get()
        )
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo(
                "Insertar",
                "Registro agregado correctamente"
            )
            limpiar()
            mostrar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        conexion.close()
def mostrar():
    for fila in tabla.get_children():
        tabla.delete(fila)
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM artesanos")
        registros = cursor.fetchall()
        for fila in registros:
            tabla.insert("", tk.END, values=fila)
        conexion.close()
def seleccionar(event):
    item = tabla.focus()
    if item:
        datos = tabla.item(item)["values"]
        txt_id.delete(0, tk.END)
        txt_nombre.delete(0, tk.END),
        txt_apellido.delete(0, tk.END)
        txt_telefono.delete(0, tk.END)
        txt_email.delete(0, tk.END)
        txt_direccion.delete(0, tk.END)
        txt_municipio.delete(0, tk.END)
        txt_descripcion.delete(0, tk.END)
        txt_pagina_web.delete(0, tk.END)
        txt_redes_sociales.delete(0, tk.END)
        
        txt_id.insert(0, datos[0])
        txt_nombre.insert(0, datos[0])
        txt_apellido.insert(0, datos[0])
        txt_telefono.insert(0, datos[0])
        txt_email.insert(0, datos[0])
        txt_direccion.insert(0, datos[0])
        txt_municipio.insert(0, datos[0])
        txt_descripcion.insert(0, datos[0])
        txt_pagina_web.insert(0, datos[0])
        txt_redes_sociales.insert(0, datos[0])   
        
def modificar():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = """
        UPDATE artesanos
        SET nombre=%s,
            apellido=%s,
            telefono=%s,
            email=%s,
            direccion=%s,
            municipio=%s,
            descripcion=%s,
            pagina_web=%s,
            redes_sociales=%s
        WHERE id_artesano=%s
        """
        valores = (
            txt_id.get(),
            txt_nombre.get(),
            txt_apellido.get(),
            txt_telefono.get(),
            txt_email.get(),
            txt_direccion.get(),
            txt_municipio.get(),
            txt_descripcion.get(),
            txt_pagina_web.get(),
            txt_redes_sociales.get()
        )
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo(
                "Modificar",
                "Registro actualizado"
            )
            mostrar()
            limpiar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        conexion.close()
def eliminar():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = "DELETE FROM artesanos WHERE id_artesano=%s"
        try:
            cursor.execute(sql, (txt_id.get(),))
            conexion.commit()
            messagebox.showinfo(
                "Eliminar",
                "Registro eliminado"
            )
            mostrar()
            limpiar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        conexion.close()
def limpiar():
        txt_id.delete(0, tk.END)
        txt_nombre.delete(0, tk.END),
        txt_apellido.delete(0, tk.END)
        txt_telefono.delete(0, tk.END)
        txt_email.delete(0, tk.END)
        txt_direccion.delete(0, tk.END)
        txt_municipio.delete(0, tk.END)
        txt_descripcion.delete(0, tk.END)
        txt_pagina_web.delete(0, tk.END) 
        txt_redes_sociales.delete(0, tk.END)
   
ventana = tk.Tk()
ventana.title("CRUD Artesanos")
ventana.geometry("1300x600")
ventana.config(bg="black")
tk.Label(ventana, text="ID",bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
txt_id = tk.Entry(ventana)
txt_id.grid(row=0, column=1)
tk.Label(ventana, text="Nombre",bg="lightblue").grid(row=1, column=0)
txt_nombre = tk.Entry(ventana)
txt_nombre.grid(row=1, column=1)
tk.Label(ventana, text="Apellido",bg="lightblue").grid(row=2, column=0)
txt_apellido = tk.Entry(ventana)
txt_apellido.grid(row=2, column=1)
#id_artesano,nombre,apellido,telefono,email,direccion,municipio,descripcion,pagina_web,redes_sociales
tk.Label(ventana, text="telefono",bg="lightblue").grid(row=3, column=0)
txt_telefono = tk.Entry(ventana)
txt_telefono.grid(row=3, column=1)
tk.Label(ventana, text="email",bg="lightblue").grid(row=4, column=0)
txt_email = tk.Entry(ventana)
txt_email.grid(row=4, column=1)
tk.Label(ventana, text="direccion",bg="lightblue").grid(row=5, column=0)
txt_direccion = tk.Entry(ventana)
txt_direccion.grid(row=5, column=1)
tk.Label(ventana, text="municipio",bg="lightblue").grid(row=6, column=0)
txt_municipio = tk.Entry(ventana)
txt_municipio.grid(row=6, column=1)
tk.Label(ventana, text="descripcion",bg="lightblue").grid(row=7, column=0)
txt_descripcion = tk.Entry(ventana)
txt_descripcion.grid(row=7, column=1)
tk.Label(ventana, text="pagina web",bg="lightblue").grid(row=8, column=0)
txt_pagina_web = tk.Entry(ventana)
txt_pagina_web.grid(row=8, column=1)
tk.Label(ventana, text="redes sociales",bg="lightblue").grid(row=9, column=0)
txt_redes_sociales = tk.Entry(ventana)
txt_redes_sociales.grid(row=9, column=1)

tk.Button(
    ventana,
    text="Probar Conexión",
    command=probar_conexion,
    bg="lightblue"
).grid(row=10, column=0, pady=10)
tk.Button(
    ventana,
    text="Insertar",
    command=insertar,
    bg="lightgreen"
).grid(row=10, column=1)
tk.Button(
    ventana,
    text="Mostrar",
    command=mostrar,
    bg="khaki"
).grid(row=10, column=2)
tk.Button(
    ventana,
    text="Modificar",
    command=modificar,
    bg="orange"
).grid(row=10, column=3)
tk.Button(
    ventana,
    text="Eliminar",
    command=eliminar,
    bg="tomato"
).grid(row=10, column=4)
tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).grid(row=10, column=5)
columnas = (
    "id_artesano",
    "nombre",
    "apellido",
    "telefono",
    "email",
    "direccion",
    "municipio",
    "descripcion",
    "pagina_web",
    "redes_sociales"
)
tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=12
)
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=120)
tabla.grid(
    row=12,
    column=0,
    columnspan=6,
    padx=10,
    pady=10
)
tabla.bind("<ButtonRelease-1>", seleccionar)
mostrar()
ventana.mainloop()