from tkinter import *
import variable.var_global as vg
import view.view_home as vh

view_root=Tk() #Inicializacion de la aplicacion

#####
view_root.overrideredirect(True) #Quitar la barra de titulos (maximizar, minimizar, cerrar)
view_root.geometry("925x500+300+100") #Para centrar la ventana
view_root.configure(bg="white") #Establecer el color del fondo
view_root.resizable(0,0) #Desabilitar el ajuste de pantalla por parte del usuario

#####
img_principal=PhotoImage(file="./img/img-principal.png")
lb_principal=Label(view_root,image=img_principal,bg="white")
lb_principal.place(x=50,y=50)

#####
f_main=Frame(view_root,width=350,height=350,bg="white")
f_main.place(x=510,y=70)

lb_title_ppal=Label(f_main,text=vg.txt_ppal,fg="#407BFF",bg="white",font=(vg.g_font,22,"bold"))
lb_title_ppal.place(x=18,y=20)

lb_title_secund=Label(f_main,text=vg.txt_secund,fg="#407BFF",bg="white",font=(vg.g_font,22),wraplength=350)
lb_title_secund.place(x=10,y=75)

btn_start=Button(f_main,width=20,pady=7,text="Comenzar",bg="#407BFF",fg="white",border=0,font=(vg.g_font,12),command=vh.vistaEstudiante)
btn_start.place(x=90,y=205)

btn_exit=Button(f_main,width=20,pady=7,text="Salir",bg="#C53F3F",fg="white",border=0,font=(vg.g_font,12),command=view_root.destroy)
btn_exit.place(x=90,y=270)

##### 
view_root.mainloop() #Para que el programa no termine