import tkinter
from tkinter import Image, ttk
from tkinter import Label

import form 

def ventanita():
    ventana = tkinter.Tk()
    ventana.geometry('500x300')
    
    #Titulo de la ventana
    ventana.title('Calculadora de Temperatura')
    #Encabezado 
    titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura') 
    titulo.pack()
    
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
            salida = confirm(0)
            salida = form.f_c(salida)
            return salida

        elif seleccion == 1:
            print("cf")
            salida = confirm(1)
            salida = form.c_f(salida)
            print(salida)
            return salida

        elif seleccion == 2:
            print("fk")
            salida = confirm(2)
            salida = form.f_k(salida)
            print(salida)
            return salida

        elif seleccion == 3:
            print("kf")
            salida = confirm(3)
            salida = form.k_f(salida)
            print(salida)
            return salida

    #La entrada del recuadro
  #  def confirm(num):

        #Subtitulo para la respuesta
        #texres = tkinter.Label(ventana, text = 'Esta es el resultado de su transformacion')
        #texres.pack()

        #Respuesta de la operacion
 #       texto = entrada.get()
        #respuesta = tkinter.PhotoImage(file = 'Transformaciones.png')
        #Label(ventana, image = respuesta, bd =0).pack(side = 'left')

        #Retorna la variable que almacena los datos de la entrada
#        return texto

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
    #sent = tkinter.Button(ventana, text = 'Procesar', command = lambda : confirm(0))
    #sent.pack()
