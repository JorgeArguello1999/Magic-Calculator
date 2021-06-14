import tkinter
from tkinter import ttk

def f_c(entrada):

    #Declaramos el lienzo y donde se va a ubicar el la respuesta
    ventana = tkinter.Tk()
    ventana.geometry('300x100')
    ventana.title('Respuesta')

    #Titulo
    titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura')
    titulo.pack()

    #Vemos si el componente funciona correctamente 
    print("conectado: ")
    entrada = float(entrada)

    #formula para determinar el resultado de la transformacion
    f = entrada
    c = (f - 32)/1.8

    #Transformamos la respuesta 'c' a typo String
    c = str(c)
    print(c)

    #Ventana de respuesta, aqui se ve la respuesta
    respuesta = tkinter.Label(ventana, text = c)
    respuesta.pack()
    texres = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
    texres.pack()

def c_f(entrada):
    
    #Declaramos el lienzo y donde se va a ubicar el la respuesta
    ventana = tkinter.Tk()
    ventana.geometry('300x100')
    ventana.title('Respuesta')

    #Titulo
    titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura')
    titulo.pack()


    #Vemos si el componente funciona correctamente 
    print("conectado: ")
    entrada = float(entrada)

    #formula para determinar el resultado de la transformacion
    c = entrada
    f = (1.8*c)+32

    #Transformamos la respuesta 'f' a typo String
    f = str(f)
    print(f)

    #Ventana de respuesta, aqui se ve la respuesta
    respuesta = tkinter.Label(ventana, text = f)
    respuesta.pack()
    texres = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
    texres.pack()

def f_k(entrada):
    
    #Declaramos el lienzo y donde se va a ubicar el la respuesta
    ventana = tkinter.Tk()
    ventana.geometry('300x100')
    ventana.title('Respuesta')

    #Titulo
    titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura')
    titulo.pack()


    #Vemos si el componente funciona correctamente 
    print("conectado: ")
    entrada = float(entrada)

    #formula para determinar el resultado de la transformacion
    f = entrada
    k = (f+459.67)/1.8 

    #Transformamos la respuesta 'f' a typo String
    k = str(k)
    print(k)

    #Ventana de respuesta, aqui se ve la respuesta
    respuesta = tkinter.Label(ventana, text = k)
    respuesta.pack()
    texres = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
    texres.pack()

def k_f(entrada):
    #Declaramos el lienzo y donde se va a ubicar el la respuesta
    ventana = tkinter.Tk()
    ventana.geometry('300x100')
    ventana.title('Respuesta')

    #Titulo
    titulo = tkinter.Label(ventana, text = 'Calculadora de Temperatura')
    titulo.pack()


    #Vemos si el componente funciona correctamente 
    print("conectado: ")
    entrada = float(entrada)

    #formula para determinar el resultado de la transformacion
    k = entrada
    f = (1.8*k)-459.67

    #Transformamos la respuesta 'f' a typo String
    f = str(f)
    print(f)

    #Ventana de respuesta, aqui se ve la respuesta
    respuesta = tkinter.Label(ventana, text = f)
    respuesta.pack()
    texres = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
    texres.pack()
