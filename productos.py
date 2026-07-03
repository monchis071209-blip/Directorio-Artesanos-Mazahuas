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
        INSERT INTO productos(id_producto,id_artesano,id_categoria,nombre_producto,descripcion_producto,precio)
        VALUES(%s,%s,%s,%s,%s,%s)
        """
        valores = (
            txt_id_producto.get(),
            txt_id_artesano.get(),
            txt_id_categoria.get(),
            txt_nombre_producto.get(),
            txt_descripcion_producto.get(),
            txt_precio.get()
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
        cursor.execute("SELECT * FROM productos")
        registros = cursor.fetchall()
        for fila in registros:
            tabla.insert("", tk.END, values=fila)
        conexion.close()
def seleccionar(event):
    item = tabla.focus()
    if item:
        datos = tabla.item(item)["values"]
        txt_id_producto.delete(0, tk.END),
        txt_id_artesano.delete(0, tk.END),
        txt_id_categoria.delete(0, tk.END),
        txt_nombre_producto.delete(0, tk.END),
        txt_descripcion_producto.delete(0, tk.END),
        txt_precio.delete(0, tk.END)
        
        txt_id_producto.insert(0, datos[0])
        txt_id_artesano.insert(0, datos[0])
        txt_id_categoria.insert(0, datos[0])
        txt_nombre_producto.insert(0, datos[0])
        txt_descripcion_producto.insert(0, datos[0])
        txt_precio.insert(0, datos[0])
def modificar():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = """
        UPDATE productos
        SET id_artesano=%s,
            id_categoria=%s,
            nombre_producto=%s,
            descripcion_producto=%s,
            precio=%s
        WHERE id_producto=%s
        """
        valores = (
        txt_id_producto.get(),
        txt_id_artesano.get(),
        txt_id_categoria.get(),
        txt_nombre_producto.get(),
        txt_descripcion_producto.get(),
        txt_precio.get()
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
        sql = "DELETE FROM productos WHERE id_producto=%s"
        try:
            cursor.execute(sql, (txt_id_producto.get(),))
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
    txt_id_producto.delete(0, tk.END),
    txt_id_artesano.delete(0, tk.END),
    txt_id_categoria.delete(0, tk.END),
    txt_nombre_producto.delete(0, tk.END),
    txt_descripcion_producto.delete(0, tk.END),
    txt_precio.delete(0, tk.END)
ventana = tk.Tk()
ventana.title("CRUD Productos")
ventana.geometry("850x500")
ventana.config(bg="black")

tk.Label(ventana, text="ID",bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
txt_id_producto = tk.Entry(ventana)
txt_id_producto.grid(row=0, column=1)
tk.Label(ventana, text="Id_Artesano",bg="lightblue").grid(row=1, column=0)
txt_id_artesano = tk.Entry(ventana)
txt_id_artesano.grid(row=1, column=1)
tk.Label(ventana, text="Id_Categoria",bg="lightblue").grid(row=2, column=0)
txt_id_categoria = tk.Entry(ventana)
txt_id_categoria.grid(row=2, column=1)
tk.Label(ventana, text="Nombre_Producto",bg="lightblue").grid(row=4, column=0)
txt_nombre_producto = tk.Entry(ventana)
txt_nombre_producto.grid(row=4, column=1)
tk.Label(ventana, text="Descripcion_Producto",bg="lightblue").grid(row=4, column=0)
txt_descripcion_producto = tk.Entry(ventana)
txt_descripcion_producto.grid(row=4, column=1)
tk.Label(ventana, text="Precio",bg="lightblue").grid(row=4, column=0)
txt_precio = tk.Entry(ventana)
txt_precio.grid(row=4, column=1)

tk.Button(
    ventana,
    text="Probar Conexión",
    command=probar_conexion,
    bg="lightblue"
).grid(row=5, column=0, pady=10)
tk.Button(
    ventana,
    text="Insertar",
    command=insertar,
    bg="lightgreen"
).grid(row=5, column=1)
tk.Button(
    ventana,
    text="Mostrar",
    command=mostrar,
    bg="khaki"
).grid(row=5, column=2)
tk.Button(
    ventana,
    text="Modificar",
    command=modificar,
    bg="orange"
).grid(row=5, column=3)
tk.Button(
    ventana,
    text="Eliminar",
    command=eliminar,
    bg="tomato"
).grid(row=5, column=4)
tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
).grid(row=5, column=5)
columnas = (
    "id_producto",
    "id_artesano",
    "id_categoria",
    "nombre_producto",
    "descripcion_producto",
    "precio"
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
    row=6,
    column=0,
    columnspan=6,
    padx=10,
    pady=10
)
tabla.bind("<ButtonRelease-1>", seleccionar)
mostrar()
ventana.mainloop()