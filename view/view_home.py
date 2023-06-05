from tkinter import *
import variable.var_global as vg
import view.view_create as vc
import view.view_read as vr
import view.view_update as vu
import view.view_delete as vd

def vistaEstudiante():
    global img_salir, img_create, img_read, img_update, img_delete

    #####
    view_student=Toplevel()
    view_student.overrideredirect(True)
    view_student.geometry("800x500+360+100")
    view_student.configure(bg="white")
    view_student.resizable(0,0)
    view_student.grab_set() #Para bloquear la ventana principal

    ############# Header
    f_header=Frame(view_student,width=800,height=100,bg="white")
    f_header.place(x=0,y=0)

    lb_title_ppal=Label(f_header,text=vg.txt_ppal,fg="#407BFF",bg="white",font=(vg.g_font,16,"bold"))
    lb_title_ppal.place(x=5,y=18)

    lb_title_secund=Label(f_header,text=vg.txt_secund,fg="#407BFF",bg="white",font=(vg.g_font,16),wraplength=600)
    lb_title_secund.place(x=5,y=50)

    img_salir = PhotoImage(file='./img/img-close.png')
    btn_salir=Button(f_header,image=img_salir,width=150,pady=7,text="Salir",bg="white",fg="black",border=0,font=(vg.g_font,12),compound=TOP,command=view_student.destroy)
    btn_salir.place(x=640,y=5)

    ############# Body
    f_body=Frame(view_student,width=800,height=300,bg="white")
    f_body.place(x=0,y=100)

    lb_title_secund=Label(f_body,text="Bienvenido :)",fg="black",bg="white",font=(vg.g_font,16))
    lb_title_secund.place(x=340,y=130)

    ############# Navbar
    f_navbar=Frame(view_student,width=800,height=100,bg="white")
    f_navbar.place(x=0,y=400)

    img_create = PhotoImage(file='./img/img-create.png')
    btn_create=Button(f_navbar,image=img_create,width=200,pady=7,text="Crear Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=BOTTOM,command=lambda:[vc.crearEstudiante(f_body),focusCreate()])
    btn_create.place(x=0,y=2)

    img_read = PhotoImage(file='./img/img-read.png')
    btn_read=Button(f_navbar,image=img_read,width=200,pady=7,text="Leer Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=BOTTOM,command=lambda:[vr.leerEstudiante(f_body),focusRead()])
    btn_read.place(x=200,y=2)

    img_update = PhotoImage(file='./img/img-update.png')
    btn_update=Button(f_navbar,image=img_update,width=200,pady=7,text="Actualizar Estudiante",bg="white",fg="black",border=0,font=(vg.g_font,10),compound=BOTTOM,command=lambda:[vu.actualizarEstudiante(f_body),focusUpdate()])
    btn_update.place(x=400,y=2)

    img_delete = PhotoImage(file='./img/img-delete.png')
    btn_delete=Button(f_navbar,image=img_delete,width=200,pady=7,text="Eliminar Estudiante",bg="SystemButtonFace",fg="black",border=0,font=(vg.g_font,10),compound=BOTTOM,command=lambda:[vd.eliminarEstudiante(f_body),focusDelete()])
    btn_delete.place(x=600,y=2)
    
    #####
    def focusCreate():
        btn_create.configure(bg="#AED6F1")
        btn_create.config(state="disabled")

        btn_read.configure(bg="white")
        btn_read.config(state="active")
        
        btn_update.configure(bg="white")
        btn_update.config(state="active")
        
        btn_delete.configure(bg="white")
        btn_delete.config(state="active")

    def focusRead():
        btn_create.configure(bg="white")
        btn_create.config(state="active")

        btn_read.configure(bg="#AED6F1")
        btn_read.config(state="disabled")
        
        btn_update.configure(bg="white")
        btn_update.config(state="active")
        
        btn_delete.configure(bg="white")
        btn_delete.config(state="active")

    def focusUpdate():
        btn_create.configure(bg="white")
        btn_create.config(state="active")

        btn_read.configure(bg="white")
        btn_read.config(state="active")
        
        btn_update.configure(bg="#AED6F1")
        btn_update.config(state="disabled")
        
        btn_delete.configure(bg="white")
        btn_delete.config(state="active")
    
    def focusDelete():
        btn_create.configure(bg="white")
        btn_create.config(state="active")

        btn_read.configure(bg="white")
        btn_read.config(state="active")
        
        btn_update.configure(bg="white")
        btn_update.config(state="active")
        
        btn_delete.configure(bg="#AED6F1")
        btn_delete.config(state="disabled")