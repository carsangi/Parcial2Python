import os
import random
from tkinter import Tk, Label, Button, Frame, Entry, X
from Dominio.Inventario import Inventario
from Dominio.Jugador import Jugador
from Infraestructura.Persistencia import Persistencia

saver = Persistencia()
saver.connect()
inventario = Inventario()
jugadorGlobal = ""
contador = 0
contFaciles = 0
contMedio = 0
contDificiles = 0
cant = 0
arrayFinal = []
saver = Persistencia()
saver.connect()
inventario = Inventario()

def close_window():
    ventana.destroy()

def signUp():

    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')

    lblId= Label(frame, text="Documento de identificación:", font="Courier")
    lblId.place(relx=0.05, rely=0.1)

    txtId = Entry(frame, font="Courier")
    txtId.place(relx=0.55,rely=0.1)

    lblNombre = Label(frame, text="Nombre:", font="Courier")
    lblNombre.place(relx=0.05, rely=0.2)

    txtNombre = Entry(frame, font="Courier")
    txtNombre.place(relx=0.55, rely=0.2)

    lblApellido = Label(frame, text="Apellido:", font="Courier")
    lblApellido.place(relx=0.05, rely=0.3)

    txtApellido = Entry(frame, font="Courier")
    txtApellido.place(relx=0.55, rely=0.3)

    lblProfesion = Label(frame, text="Profesion:", font="Courier")
    lblProfesion.place(relx=0.05, rely=0.4)

    txtProfesion = Entry(frame, font="Courier")
    txtProfesion.place(relx=0.55, rely=0.4)

    lblPassword = Label(frame, text="Contraseña:", font="Courier")
    lblPassword.place(relx=0.05, rely=0.5)

    txtPassword = Entry(frame, font="Courier")
    txtPassword.place(relx=0.55, rely=0.5)


    def guardar():
        if txtId.get() == "" or txtNombre.get() == "" or txtApellido.get() == "" or txtProfesion.get() == "" or txtPassword.get() == "":
            print("Complete los espacios")
        else:
            jugador = Jugador(txtId.get(),txtNombre.get(),txtApellido.get(),txtProfesion.get(),"null",txtPassword.get())
            saver.guardar_bd(jugador)
            saver.save_json(jugador)
            print("Guardado con éxito")
            frame.destroy()

    btnGuardar = Button(frame, text="Guardar", bg="green", fg="white", font="Courier", command=guardar)
    btnGuardar.place(relx=0.1, rely=0.85, relwidth=0.30, relheight=0.1)

    btnCerrar = Button(frame, text="Atras", bg="green", fg="white",font="Courier", command=frame.destroy)
    btnCerrar.place(relx=0.55, rely=0.85, relwidth=0.30, relheight=0.1)


def gano(jugadorGlobal):
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblText = Label(frame,
                              text="Felicitaciones: " + jugadorGlobal.nombre + " " + jugadorGlobal.apellido + "\nHas Ganado",
                              font="Courier")
    lblText.place(relx=0.1, rely=0.5)


def perdio(jugadorGlobal):
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblText = Label(frame, text="Lo Lamento: " + jugadorGlobal.nombre + " " + jugadorGlobal.apellido + "\nHas Perdido",
                       font="Courier")
    lblText.place(relx=0.1, rely=0.5)


def preguntas(jugadorGlobal, cant):
    global contador
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')
    lblPregunta = Label(frame, text="Pregunta " + str((contador + 1)) + ":", font="Courier")
    lblPregunta.place(relx=0.1, rely=0.05)

    Seguro = Label(frame, text="", font="Courier")
    Seguro.place(relx=0.1, rely=0.15)

    if cant == 10:
        if contador == 2 or contador == 5 or contador == 8:
            Seguro['text'] = "Pregunta Seguro"

    elif cant == 11:
        if contador == 3 or contador == 6 or contador == 9:
            Seguro['text'] = "Pregunta Seguro"
    elif cant == 16:

        if contador == 4 or contador == 9 or contador == 14:
            Seguro['text'] = "Pregunta Seguro"

    def elecciona():
        global contador

        eleccion = a['text']
        res = pre.respuesta
        if eleccion == res:

            print("Respuesta Correcta")
            frame.destroy()
            contador += 1

            if (contador == len(arrayFinal)):
                gano(jugadorGlobal)

                frame.destroy()
            else:
                preguntas(jugadorGlobal, cant)
                frame.destroy()

        else:
            perdio(jugadorGlobal)
            frame.destroy()

    def eleccionb():
        global contador

        eleccion = b['text']
        res = pre.respuesta
        if eleccion == res:

            print("Respuesta Correcta")
            frame.destroy()
            contador += 1
            if (contador == len(arrayFinal)):
                gano(jugadorGlobal)

                frame.destroy()
            else:
                preguntas(jugadorGlobal, cant)
                frame.destroy()

        else:
            perdio(jugadorGlobal)
            frame.destroy()

    def eleccionc():

        global contador

        eleccion = c['text']
        res = pre.respuesta
        if eleccion == res:

            print("Respuesta Correcta")
            frame.destroy()
            contador += 1
            if (contador == len(arrayFinal)):
                gano(jugadorGlobal)

                frame.destroy()
            else:
                preguntas(jugadorGlobal, cant)
                frame.destroy()

        else:
            perdio(jugadorGlobal)
            frame.destroy()

    def elecciond():
        global contador

        eleccion = d['text']
        res = pre.respuesta
        if eleccion == res:

            print("Respuesta Correcta")
            frame.destroy()
            contador += 1
            if (contador == len(arrayFinal)):
                gano(jugadorGlobal)
                frame.destroy()
            else:
                preguntas(jugadorGlobal, cant)
                frame.destroy()
        else:
            perdio(jugadorGlobal)
            frame.destroy()

    a = Button(frame, bg="green", fg="white", font="Courier", command=elecciona)
    a.place(relx=0.02, rely=0.4, relwidth=0.5, relheight=0.15)

    b = Button(frame, bg="green", fg="white", font="Courier", command=eleccionb)
    b.place(relx=0.47, rely=0.4, relwidth=0.5, relheight=0.15)

    c = Button(frame, bg="green", fg="white", font="Courier", command=eleccionc)
    c.place(relx=0.02, rely=0.6, relwidth=0.5, relheight=0.15)

    d = Button(frame, bg="green", fg="white", font="Courier", command=elecciond)
    d.place(relx=0.47, rely=0.6, relwidth=0.5, relheight=0.15)

    pre = arrayFinal[contador]
    lblPregunta['text'] += " " + pre.enunciado
    a['text'] = pre.opcion_a
    b['text'] = pre.opcion_b
    c['text'] = pre.opcion_c
    d['text'] = pre.opcion_d


def cargarPreguntas(facil, medio, dificil):
    global contFaciles
    global contDificiles
    global contMedio
    arrayFinal.clear()
    total = facil + medio + dificil
    array = []
    for i in inventario.preguntas:
        array.append(i)
    for i in inventario.preguntas:

        if len(arrayFinal) < total:
            num = random.randint(0, len(array) - 1)

            if array[num].dificultad == "Facil":

                if contFaciles < facil:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.id_pregunta == i.id_pregunta:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contFaciles += 1

            if array[num].dificultad == "Intermedio":

                if contMedio < medio:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.id_pregunta == i.id_pregunta:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contMedio += 1
            if array[num].dificultad == "Dificil":

                if contDificiles < dificil:
                    if len(arrayFinal) == 0:
                        arrayFinal.append(array[num])
                    else:
                        esta = False
                        for k in arrayFinal:
                            if k.id_pregunta == i.id_pregunta:
                                esta = True
                                break
                            else:
                                pass
                        if esta:
                            pass
                        else:

                            arrayFinal.append(array[num])
                            contDificiles += 1

def cargar_file():
    global jugador
    global contador
    global contFaciles
    global contMedio
    global contDificiles
    global arrayFinal
    inventario.eliminarListas()
    for file in os.listdir("./Files"):
        if '.json' in file:
            inventario.agregar_objeto(saver.load_json(file))

def juego(jugadorGlobal):
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')

    lblJugador = Label(frame, text="Jugador:", font="Courier")
    lblJugador.place(relx=0.25, rely=0.05)

    lblJugador1 = Label(frame, text=jugadorGlobal.nombre + " " + jugadorGlobal.apellido, font="Courier")
    lblJugador1.place(relx=0.45, rely=0.05)

    lbl2=Label(frame,text="Elija la cantidad de preguntas", font="Courier 15")
    lbl2.place(relx=0.17, rely=0.25)

    lbl2 = Label(frame, text="                          ", font="Courier 16")
    lbl2.place(relx=0.47, rely=0.4)

    def cant1():
        text1=preguntas10['text']
        lbl2['text'] = text1

        cargarPreguntas(3,5,2)

    def cant2():
        text1=preguntas11['text']
        lbl2['text'] = text1
        cargarPreguntas(3, 5, 3)
    def cant3():
        text1=preguntas16['text']
        lbl2['text'] = text1
        cargarPreguntas(5, 5, 6)

    def continuar():
        cant = int(lbl2['text'])
        preguntas(jugadorGlobal,cant)
        frame.destroy()

    preguntas10=Button(frame, text="10", bg="green", fg="white", font="Courier", command=cant1)
    preguntas10.place(relx=0.17, rely=0.55, relwidth=0.2, relheight=0.15)

    preguntas11 = Button(frame, text="11", bg="green", fg="white", font="Courier", command=cant2)
    preguntas11.place(relx=0.40, rely=0.55, relwidth=0.2, relheight=0.15)

    preguntas16 = Button(frame, text="16", bg="green", fg="white", font="Courier", command=cant3)
    preguntas16.place(relx=0.63, rely=0.55, relwidth=0.2, relheight=0.15)

    continuar = Button(frame, text="Siguente", bg="green", fg="white", font="Courier" ,command=continuar)
    continuar.place(relx=0.27, rely=0.7, relwidth=0.21, relheight=0.15)

    salir = Button(frame, text="Atras", bg="green", fg="white", font="Courier" ,command=frame.destroy)
    salir.place(relx=0.52, rely=0.7, relwidth=0.20, relheight=0.15)

def signIn():
    cargar_file()
    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')

    lblId_Jugador = Label(frame, text="Ingrese Documento de Identificación", font="Courier")
    lblId_Jugador.pack(pady=10)

    txtId_Jugador = Entry(frame, font="Courier")
    txtId_Jugador.pack()

    lblPassword = Label(frame, text="Ingrese su contraseña", font="Courier")
    lblPassword.pack()

    txtPassword = Entry(frame, font="Courier", show="*")
    txtPassword.pack(pady=10)

    etiqueta2 = Label(frame)
    etiqueta2.pack()

    def buscar_objeto():
        id_jugador = txtId_Jugador.get()
        password = txtPassword.get()
        if len(list(inventario.buscarJugadorDocumento(id_jugador,password))) == 0:
            print("\nDocumento de identidad o Contraseña incorrecta\n")
        else:
            jugadores = list(inventario.buscarJugadorDocumento(id_jugador,password))
            for i in jugadores:
                for file in os.listdir("./Files"):
                    if ''+i.id_jugador+'.json' in file:
                        jugadorGlobal = saver.load_json(file)

            juego(jugadorGlobal)
            frame.destroy()

    signIn = Button(frame, text="Sign In",bg="green" ,fg="white", command= buscar_objeto)
    signIn.place(relx=0.25,rely=0.8, relwidth=0.20 , relheight=0.15)

    atras = Button(frame, text="Atras", bg="green", fg="white", command=frame.destroy)
    atras.place(relx=0.55, rely=0.8, relwidth=0.20, relheight=0.15)

ventana = Tk()
ventana.geometry("890x400")
btnLogin=Button(ventana,text = "Sign in",bg="green",fg="white" , font="Courier",command = signIn)
btnLogin.place(relx=0.3,rely = 0.3,relwidth=0.40, relheight=0.15)
btnsignup=Button(ventana,text = "Sign Up",bg="green" ,fg="white", font="Courier",command = signUp)
btnsignup.place(relx=0.3,rely = 0.5, relwidth=0.40, relheight=0.15)
ventana.title("Quien Quiere Ser Millonario - Parcial 2 Phyton")
etiqueta = Label(ventana,text="Bienvenido Futuro Millonario", bg="green" , fg="white", font="Courier")
etiqueta.pack(fill = X)
ventana.mainloop()

if __name__ == '__main__':
    saver = Persistencia()
    saver.connect()
    inventario = Inventario()
    cargar_file()

