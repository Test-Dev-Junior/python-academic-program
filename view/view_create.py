from tkinter import *
import variable.var_global as vg
import model.conn as db
from tkinter import messagebox

def crearEstudiante(f_body):

    global img_save

    #####Frame Description
    f_description=Frame(f_body,width=200,height=300,bg="#407BFF")
    f_description.place(x=0,y=0)

    lb_title_ppal=Label(f_description,text="Crear Estudiante",fg="white",bg="#407BFF",font=(vg.g_font,16,"bold"))
    lb_title_ppal.place(x=10,y=80)
    
    lb_title_secund=Label(f_description,text="Para ingresar un estudiante al sistema por favor llenar el siguiente formulario",fg="black",bg="#407BFF",font=(vg.g_font,12),wraplength=190)
    lb_title_secund.place(x=15,y=120)

    #####Frame Form
    f_form=Frame(f_body,width=600,height=300,bg="#5DADE2")
    f_form.place(x=200,y=0)

    ##
    lb_name=Label(f_form,text="Nombre: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_name.place(x=70,y=30)

    et_name=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_name.place(x=180,y=30)

    ##
    lb_lastname=Label(f_form,text="Apellido: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_lastname.place(x=70,y=90)

    et_lastname=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_lastname.place(x=180,y=90)

    ##
    lb_age=Label(f_form,text="Edad: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_age.place(x=70,y=150)

    et_age=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_age.place(x=180,y=150)

    def insertarEstudiante():
        if et_name.get() != "" and et_age.get() != "" and et_lastname.get() != "":
            if (any(chr.isdigit() for chr in et_name.get()) != True):
                if (any(chr.isdigit() for chr in et_lastname.get()) != True):
                    if et_age.get().isnumeric():
                        edad=et_age.get()
                        apellido=et_lastname.get()
                        nombre=et_name.get()
                        db.insertarDatos(nombre,apellido,edad)

                        et_name.delete(0,END)
                        et_lastname.delete(0,END)
                        et_age.delete(0,END)
                    else:
                        messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar un número en el campo edad")
                else:
                    messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar texto en el campo apellido") 
            else:
                messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar texto en el campo nombre")    
        else:
            messagebox.showerror(title="Error de ingreso de datos",message="Por favor llene todos los campos")

    ##
    img_save = PhotoImage(file='./img/img-save.png')
    btn_read=Button(f_form,image=img_save,width=200,pady=7,text="Guardar Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=LEFT,command=insertarEstudiante)
    btn_read.place(x=200,y=220)