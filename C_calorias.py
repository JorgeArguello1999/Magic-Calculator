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

    #Recuadro de la entrada del peso 
    subtitle = tkinter.Label(ventana, text = 'Ingrese su peso en KiloGramos (Kg)')
    subtitle.pack()

    peso= tkinter.Entry(ventana)
    peso.focus()
    peso.pack()

    #Entrada de Datos de altura
    subtitle1 = tkinter.Label(ventana, text = 'Ingrese su Altura en CentiMetros (Cm)')
    subtitle1.pack()

    altura = tkinter.Entry(ventana)
    altura.pack()

    #Entrada de Datos de Edad
    subtitle1 = tkinter.Label(ventana, text = 'Ingrese su Edad en Años')
    subtitle1.pack()

    edad = tkinter.Entry(ventana)
    edad.pack()

    #Subtitulo para la eleccion de genero
    subtitle2 = tkinter.Label(ventana, text = 'Selecciona tu Genero')
    subtitle2.pack()

    #Boton para Genero Femenino
    femenino = tkinter.Button(ventana, text = 'Femenino', command = lambda : confirm(1))
    femenino.pack()

    #Boton para Genero Masculino
    masculino = tkinter.Button(ventana, text = 'Masculino', command = lambda : confirm(2))
    masculino.pack()

    #Obtenemos los datos de cada entrada
    def confirm (num):

        #Aqui se va a presenciar un codigo totalmente innecesario, por el momento se va a quedar asi
        #me refiero a crear una nueva ventana con la respuesta

        peso1 = peso.get()
        altura1 = altura.get()
        edad1 = edad.get()

        #Transformamos los valores a floats o str
        peso1 = float(peso1)
        altura1 = float(altura1)
        edad1 = float(edad1)

        #Comprobamos la entrada de los datos
        print(peso1, altura1, edad1)       

        #selector de genero
        if num == 1:
            print('mujer')
            respuesta = (10*peso1)+(6.25*altura1)-(5*edad1)-161
            respuesta = str(respuesta)
            print(respuesta)

            #Creamos la ventana
            ventana = tkinter.Tk()
            ventana.geometry('500x300')

            #Titulo de la ventana
            titulo = tkinter.Label(ventana, text = 'Calculadora de Calorias')
            titulo.pack()

           
            ventana.title('Respuesta')

            texto = tkinter.Label(ventana, text = respuesta)
            texto.pack()

            texto_fin = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
            texto_fin.pack()


        elif num == 2:
            print('hombre')
            respuesta = (10*peso1)+(6.25*altura1)-(5*edad1) + 5
            respuesta = str(respuesta)
            print(respuesta)

            #Creamos la ventana
            ventana = tkinter.Tk()
            ventana.geometry('500x300')
            
            #Titulo de la ventana
            titulo = tkinter.Label(ventana, text = 'Calculadora de Calorias')
            titulo.pack()

            ventana.title('Respuesta')

            texto = tkinter.Label(ventana, text = respuesta)
            texto.pack()

            texto_fin = tkinter.Label(ventana, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
            texto_fin.pack()


    #Boton para el envio de Datos
    #boton = tkinter.Button(ventana, text = 'Enviar Datos', command = confirm(0))
    #boton.pack()

