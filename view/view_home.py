from tkinter import *
import variable.var_global as vg

def vistaEstudiante():
    global img_salir

    #####
    view_student=Toplevel()
    view_student.overrideredirect(True)
    view_student.geometry("800x500+360+100")
    view_student.configure(bg="white")
    view_student.resizable(0,0)

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
    f_body=Frame(view_student,width=800,height=300,bg="blue")
    f_body.place(x=0,y=100)

    ############# Navbar
    f_navbar=Frame(view_student,width=800,height=100,bg="green")
    f_navbar.place(x=0,y=400)