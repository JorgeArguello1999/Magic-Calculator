import tkinter
from tkinter import ttk

import formulas 

def ventanita():
    ventana = tkinter.Tk()
    ventana.geometry('500x500')
    
    #Titulo de la ventana
    ventana.title('Calculadora de Temperatura')
#Encabezado titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura') titulo.pack()

    #Nombre de la Entrada
    subtitle = tkinter.Label(ventana, text = 'Ingresa el Numero y Posteriormente')
    subtitle.pack()

    #Recuadro para la entrada de datos
    entrada = tkinter.Entry(ventana)
    entrada.focus()
    entrada.pack()
    
    #Funcion para el redireccionamiento de las opciones
    def selector(seleccion):
        
        #Aqui se usa el modulo correspondiente dependiendo la opcion elegida
        if seleccion == 0:
            print("fc")
            formulas.f_c()

        elif seleccion == 1:
            print("cf")

        elif seleccion == 2:
            print("fk")

        elif seleccion == 3:
            print("kf")

    #La entrada del recuadro
    def confirm(num):
        #Subtitulo para la respuesta
        texres = tkinter.Label(ventana, text = 'Esta es el resultado de su transformacion')
        texres.pack()

        #Respuesta de la operacion
        texto = entrada.get()
        respuesta = tkinter.Label(ventana, text = texto)
        respuesta.pack()

    #Fahrenheit a Celsius
    F_C = tkinter.Button(ventana, text = 'Fahrenheit a Celsius', command = lambda : selector(0))
    F_C.pack()
    
    #Celsius a Fahrenheit
    C_F = tkinter.Button(ventana, text = 'Celsius a Fahrenheit', command = lambda : selector(1))
    C_F.pack()
 
    #Fahrenheit a Kelvin
    F_K = tkinter.Button(ventana, text = 'Fahrenheit a Kelvin', command = lambda : selector(2))
    F_K.pack()

    #Kelvin a Fahrenheit
    K_F = tkinter.Button(ventana, text = 'Kelvin a Fahrenheit', command = lambda : selector(3))
    K_F.pack()

    #Envio de datos
    sent = tkinter.Button(ventana, text = 'Procesar', command = lambda : confirm(0))
    sent.pack()
