import psycopg2
from tkinter import messagebox

connection=psycopg2.connect(
    host="localhost",
    user="postgres",
    password="SalinasEdison08",
    database="bd_programa_academico",
    port="5432"
)

connection.autocommit = True

def crearTabla():
    cursor=connection.cursor()
    query="CREATE TABLE tb_estudiante(id SERIAL, nombre varchar(25), apellido varchar(25), edad int)"
    try:
        cursor.execute(query)
    except:
        print("La tabla ya existe")
    cursor.close()

#crearTabla()

def insertarDatos(nombre,apellido,edad):
    cursor=connection.cursor()
    query=f""" INSERT INTO tb_estudiante(nombre,apellido,edad) values ('{nombre}','{apellido}',{edad})"""
    try:
        cursor.execute(query)
        messagebox.showinfo(title="Guardado de datos",message="Se guardaron los datos exitosamente")
    except:
        messagebox.showerror(title="Guardado de datos",message="Se produjo un error con la conexión de la DB al intentar guardar los datos")
        #print("Se produjo un error con la conexión de la DB al intentar guardar los datos")
    cursor.close()

def leerDatos():
    cursor=connection.cursor()
    query="SELECT * FROM tb_estudiante"
    try:
        cursor.execute(query)
        arr_students=cursor.fetchall()
        messagebox.showinfo(title="Recuperación de datos",message="Se recuperaron los datos exitosamente")
        return arr_students
    except:
        messagebox.showerror(title="Guardado de datos",message="Se produjo un error con la conexión de la DB al intentar recuperar los datos")
        #print("Se produjo un error con la conexión de la DB al intentar recuperar los datos")
    cursor.close()

def actualizarDatos(id,nombre,apellido,edad):
    cursor=connection.cursor()
    query=f""" UPDATE tb_estudiante set nombre='{nombre}',apellido='{apellido}',edad={edad} where id='{id}'"""
    try:
        cursor.execute(query)
        messagebox.showinfo(title="Actualización de datos",message="Se actualizaron los datos exitosamente")
    except:
        messagebox.showerror(title="Actualización de datos",message="Se produjo un error con la conexión de la DB al intentar actualizar los datos")
        #print("Se produjo un error con la conexión de la DB al intentar actualizar los datos")
    cursor.close()

def leerDatosId(id):
    cursor=connection.cursor()
    query=f""" SELECT * FROM tb_estudiante where id='{id}' """
    try:
        cursor.execute(query)
        arr_students=cursor.fetchone()
        messagebox.showinfo(title="Recuperación de datos",message="Se recuperaron los datos exitosamente")
        return arr_students
    except:
        messagebox.showerror(title="Guardado de datos",message="Se produjo un error con la conexión de la DB al intentar recuperar los datos")
        #print("Se produjo un error con la conexión de la DB al intentar recuperar los datos")
    cursor.close()

def eliminarDatosId(id):
    cursor=connection.cursor()
    query=f""" DELETE FROM tb_estudiante where id='{id}' """
    try:
        cursor.execute(query)
        messagebox.showinfo(title="Eliminación de datos",message="Se elimino el registro exitosamente")
    except:
        messagebox.showerror(title="Eliminación de datos",message="Se produjo un error con la conexión de la DB al intentar eliminar el registro")
        #print("Se produjo un error con la conexión de la DB al intentar eliminar el registro")
    cursor.close()