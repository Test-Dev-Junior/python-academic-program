from tkinter import *
import variable.var_global as vg
import model.conn as db
from tkinter import messagebox
from tkinter import ttk

def eliminarEstudiante(f_body):

    global img_delete,img_find

    #####Frame Description
    f_description=Frame(f_body,width=200,height=300,bg="#407BFF")
    f_description.place(x=0,y=0)

    lb_title_ppal=Label(f_description,text="Eliminar Estudiante",width=12,fg="white",bg="#407BFF",font=(vg.g_font,16,"bold"),wraplength=200)
    lb_title_ppal.place(x=10,y=50)
    
    lb_title_secund=Label(f_description,text="Para eliminar un estudiante en el sistema por favor seleccione el ID",width=15,fg="black",bg="#407BFF",font=(vg.g_font,12),wraplength=150)
    lb_title_secund.place(x=20,y=120)

    #####Frame Form
    f_form=Frame(f_body,width=600,height=300,bg="#5DADE2")
    f_form.place(x=200,y=0)

    ##
    lb_id=Label(f_form,text="ID: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_id.place(x=70,y=20)

    et_id=ttk.Combobox(f_form,font=(vg.g_font,14),width=13,state="readonly")
    et_id.place(x=180,y=20)

    def recuperarID():
        arr_students=db.leerDatos()
        student=[]
        for row in arr_students:
            student.append(row[0])
        return student
    
    et_id["values"]=recuperarID()
    
    ##
    lb_name=Label(f_form,text="Nombre: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_name.place(x=70,y=70)

    et_name=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_name.place(x=180,y=70)

    ##
    lb_lastname=Label(f_form,text="Apellido: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_lastname.place(x=70,y=120)

    et_lastname=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_lastname.place(x=180,y=120)

    ##
    lb_age=Label(f_form,text="Edad: ",fg="white",bg="#5DADE2",font=(vg.g_font,14,"bold"))
    lb_age.place(x=70,y=170)

    et_age=Entry(f_form,border=0,font=(vg.g_font,14),width=30)
    et_age.place(x=180,y=170)

    et_name.configure(state="disabled")
    et_lastname.configure(state="disabled")
    et_age.configure(state="disabled")

    ##
    def recuperarDatos():
        id_student=0
        if et_id.get() != "":
            id_student=int(et_id.get())
            if(id_student != 0):
                arr_students=db.leerDatosId(id_student)
                if(len(arr_students)!=0):
                    ###
                    et_name.configure(state="normal")
                    et_lastname.configure(state="normal")
                    et_age.configure(state="normal")

                    et_name.delete(0,END)
                    et_lastname.delete(0,END)
                    et_age.delete(0,END)

                    ###
                    et_name.insert(0, arr_students[1])
                    et_lastname.insert(0, arr_students[2])
                    et_age.insert(0, arr_students[3])

                    et_name.configure(state="disabled")
                    et_lastname.configure(state="disabled")
                    et_age.configure(state="disabled")

                    btn_delete.configure(state="active")
        else:
            messagebox.showwarning(title="Selección de ID",message="Por favor debe seleccionar un ID de estudiante")

      ##
    def eliminarEstudiante():
        if et_id.get() != "":
            if et_name.get() != "" and et_age.get() != "" and et_lastname.get() != "":
                if (any(chr.isdigit() for chr in et_name.get()) != True):
                    if (any(chr.isdigit() for chr in et_lastname.get()) != True):
                        if et_age.get().isnumeric():
                            id=et_id.get()

                            db.eliminarDatosId(id)

                            et_id.configure(state="normal")
                            et_id.delete(0,END)
                            et_id.configure(state="readonly")

                            et_name.configure(state="normal")
                            et_name.delete(0,END)
                            et_name.configure(state="disabled")
                            
                            et_lastname.configure(state="normal")
                            et_lastname.delete(0,END)
                            et_lastname.configure(state="disabled")
                            
                            et_age.configure(state="normal")
                            et_age.delete(0,END)
                            et_age.configure(state="disabled")

                            et_id["values"]=recuperarID()

                        else:
                            messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar un número en el campo edad")
                    else:
                        messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar texto en el campo apellido") 
                else:
                    messagebox.showwarning(title="Tipo de dato inválido",message="Por favor debe ingresar texto en el campo nombre")    
            else:
                messagebox.showerror(title="Error de ingreso de datos",message="Por favor llene todos los campos")
        else:
            messagebox.showerror(title="Error de selección de ID",message="Por favor seleccione el ID del estudiante")
    
    ##
    img_delete = PhotoImage(file='./img/img-delete-2.png')
    btn_delete=Button(f_form,image=img_delete,state="disabled",width=200,pady=7,text="Eliminar Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=LEFT,command=eliminarEstudiante)
    btn_delete.place(x=200,y=220)

    ##
    img_find = PhotoImage(file='./img/img-find.png')
    btn_find=Button(f_form,image=img_find,width=150,pady=3,text="Buscar Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=LEFT,command=recuperarDatos)
    btn_find.place(x=360,y=20)