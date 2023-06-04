import psycopg2

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
    query="CREATE TABLE tb_estudiante(id int, nombre varchar(25), apellido varchar(25), edad int)"
    try:
        cursor.execute(query)
    except:
        print("La tabla ya existe")
    cursor.close()

crearTabla()