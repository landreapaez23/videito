import tkinter
ventana= tkinter.Tk()
ventana.title("Viva Temu")
ventana.iconbitmap("Dinero.ico")
ventana.geometry("1920x1080+0+0")
ventana.minsize(600,400)
ventana.maxsize(1250, 1000)
ventana.resizable(False,True)
ventana.configure(bg= "light blue")
ventana.attributes("-alpha",0.8)
cuadro1= tkinter.Frame(ventana)
cuadro1.configure(width= 300, height= 280, bg= "aquamarine2", bd= 20)
cuadro1.pack()
cuadro2= tkinter.Frame(ventana)
cuadro2.configure(width= 300, height= 280, bg= "pink1", bd= 20)
cuadro2.pack()
def comprar():
    print("Compra en temu, gasta tus ahorros en mi")
boton= tkinter.Button(cuadro1, text= "Compra", command= comprar)
boton.pack()

ventana.mainloop()
print ("haga la ventana pues")
def convertirTextoMayus(texto):
    print(texto.upper())

convertirTextoMayus("haga la ventana yaaa")
