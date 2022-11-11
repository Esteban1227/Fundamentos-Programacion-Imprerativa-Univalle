from tkinter import *
def menu():
    #lista de elemetos
    elementosDisponibles = {
        "deporte":[
        ],
        "cultural":[
        ]
    }
    raiz = Tk()
    titulo = Label(raiz, text="Bienestar")
    frameDeporte = Frame(raiz, bg="blue")
    botonAgregarDeporte = Button(frameDeporte, text="Agregar elemento deportivo", command= lambda: menuAgregarElemento(frameDeporte, elementosDisponibles["deporte"]))
    frameCultural = Frame(raiz, bg="red")
    botonAgregarCultural = Button(frameCultural, text="Agregar elemento Cultural", command= lambda: menuAgregarElemento(frameCultural, elementosDisponibles["cultural"]))
    botonSalir = Button(raiz, text="Salir", command= lambda: cerrar(raiz))
    titulo.pack()
    frameDeporte.pack()
    botonAgregarDeporte.pack()
    frameCultural.pack()
    botonAgregarCultural.pack()
    botonSalir.pack()
    raiz.mainloop()
    #cuando se agregue un nuevo elemento sumar a la cantidad 1
    #si la cantidad es 0 avisar
    #modificar los datos

def menuAgregarElemento(frame, categoriaEspecifica):
    raizAgregarElemento = Tk()
    titulo = Label(raizAgregarElemento, text="Bienestar")
    labelEntryNombre = Label(raizAgregarElemento, text="Nombre")
    entryNombre = Entry(raizAgregarElemento)
    labelEntryCantidad = Label(raizAgregarElemento, text="Cantidad del elemento")
    entryCantidad = Entry(raizAgregarElemento)
    botonAceptar = Button(raizAgregarElemento, text="Agregar", command= lambda: agregarElemento(frame, raizAgregarElemento, categoriaEspecifica, entryNombre.get(), int(entryCantidad.get())))
    botonSalir = Button(raizAgregarElemento, text="Salir", command= lambda: cerrar(raizAgregarElemento))
    titulo.pack()
    labelEntryNombre.pack()
    entryNombre.pack()
    labelEntryCantidad.pack()
    entryCantidad.pack()
    botonAceptar.pack()
    botonSalir.pack()

def cerrar(raiz):
    raiz.destroy()

def agregarElemento(frame, raizCerrar, categoriaEspecifica, entryNombre, entryCantidad):
    cerrar(raizCerrar)
    categoriaEspecifica.append([entryNombre, entryCantidad])
    elementoFrame = Frame(frame)
    labelNombre = Label(frame, text=entryNombre)
    labelCantidad = Label(frame, text=entryCantidad)
    labelNombre.pack()
    labelCantidad.pack()
    elementoFrame.pack()
    
menu()