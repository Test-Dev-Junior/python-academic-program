from tkinter import *
import variable.var_global as vg
import model.conn as db
from tkinter import ttk

def leerEstudiante(f_body):

    arr_students=db.leerDatos()

    #####Frame Description
    f_description=Frame(f_body,width=200,height=300,bg="#407BFF")
    f_description.place(x=0,y=0)

    lb_title_ppal=Label(f_description,text="Leer Estudiante",fg="white",bg="#407BFF",font=(vg.g_font,16,"bold"))
    lb_title_ppal.place(x=10,y=80)
    
    lb_title_secund=Label(f_description,text="Se muestran los datos de los estudiantes guardados en la base de datos",fg="black",bg="#407BFF",font=(vg.g_font,12),wraplength=190)
    lb_title_secund.place(x=15,y=120)

    #####Frame Tabla
    f_table=Frame(f_body,width=600,height=300,bg="#5DADE2")
    f_table.place(x=200,y=0)

    ##
    col_table=("id","name","last_name","age") #Definir columnas de la tabla

    tb_student=ttk.Treeview(f_table,columns=col_table,show="headings")

    #Dimensiones de los encabezados
    tb_student.column("id",width=145,anchor=CENTER)
    tb_student.column("name",width=145,anchor=CENTER)
    tb_student.column("last_name",width=145,anchor=CENTER)
    tb_student.column("age",width=145,anchor=CENTER)

    #Definir titulos de los encabezados
    tb_student.heading("id",text="ID")
    tb_student.heading("name",text="Nombre")
    tb_student.heading("last_name",text="Apellido")
    tb_student.heading("age",text="Edad")

    #Definir Tags para tabla colorida
    tb_student.tag_configure("color_pri",background="#D4E6F1")
    tb_student.tag_configure("color_sec",background="white")

    count=0

    for student in arr_students:
        if count % 2 == 0:
            tb_student.insert("",END,text="",values=(student[0],student[1],student[2],student[3]),tags="color_pri")
        else:
            tb_student.insert("",END,text="",values=(student[0],student[1],student[2],student[3]),tags="color_sec")
        count+=1

    tb_student.place(x=8,y=5)