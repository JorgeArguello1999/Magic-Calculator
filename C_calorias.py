import tkinter 
from tkinter import Label
from tkinter import Image, ttk

#La formula viene a ser la siguiente
###Mujer = (10 * pesoKg) + (6.25 * estaturaCM) - (5 * edadAños) - 161
    ###Hombre = (10 * pesoKg) + (6.25 * estaturaCM) - (5 * edadAños) + 5

def ventana():
    
    #Iniciamos el objeto para la ventana
    ventana = tkinter.Tk()
    ventana.geometry ('500x300')

    #Titulo de la ventana
    ventana.title('Calculadora de Calorias')
    
    #Encabezado 
    titulo = tkinter.Label(ventana, text = 'Calculadora de Calorias')
    titulo.pack

    #Nombre de la Entrada de Datos
    subtitle = tkinter.Label(ventana, text = 'Ingrese su peso en KiloGramos (Kg)')
    subtitle.pack()

    #Recuadro de la entrada del peso 
    peso= tkinter.Entry(ventana)
    peso.focus()
    peso.pack()
    peso = peso.get()

    #Entrada de Datos de altura
    altura = tkinter.Entry(ventana)
    altura.pack()
    altura = altura.get()

    #Entrada de Datos de Edad
    edad = tkinter.Entry(ventana)
    edad.pack()
    edad = edad.get()

    #Entrada de Datos para Genero
    genero = tkinter.Entry(ventana)
    genero.pack()
    genero = genero.get()

    #Boton para el envio de Datos
    boton = tkinter.Button(ventana, text = 'Enviar Datos', command = lambda : procesos(peso, altura, edad, genero))
    boton.pack()

def procesos(peso, altura, edad, genero):
    peso = float(peso)
    edad = float(edad)
    matd = peso -2
    print(matd)
