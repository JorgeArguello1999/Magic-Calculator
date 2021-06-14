import tkinter
from tkinter import ttk, Label, Image

def ventana():

    #Parametros del lienzo
    ventana = tkinter.Tk()
    ventana.geometry('500x300')
    ventana.title('Calculadora de Porcentaje')

    #Titulo
    titulo = tkinter.Label(ventana, text = 'Calculadora de Porcentaje')
    titulo.pack()

    #Primera entrada de los datos 
    subtitle = tkinter.Label(ventana, text = 'Ingrese el valor del cual necesita saber el porcentaje')
    subtitle.pack()
    #->Entrada del valor de que queremos saber su porcentaje
    valor = tkinter.Entry(ventana)
    valor.pack()

    #Segunda entrada de los datos
    subtitle1 = tkinter.Label(ventana, text = 'Ingrese el Porcentaje que necesita saber del valor indicado')
    subtitle1.pack()
    #->Entrada del porcentaje que queremos saber
    porcen = tkinter.Entry(ventana)
    porcen.pack()

    def confirm():
        
        #Obtenemos los datos de la entrada del primer valor 'valor'
        primervalor = valor.get()
        primervalor = float(primervalor)
        print(primervalor)

        porcentaje = porcen.get()
        porcentaje = float(porcentaje)
        print(porcentaje)

        #Codigo innecesario pero por el momento util para terminar el proyecto
        resultado = (primervalor*porcentaje)/100
        resultado = str(resultado)
        print(resultado)

        ventanita = tkinter.Tk()
        ventanita.geometry('300x500')
        ventanita.title('Respuesta')

        #titulo
        titulo = tkinter.Label(ventanita, text = 'Calculadora de porcentaje')
        titulo.pack()

        #recuadro emergente para el resultado
        cuad_resultado = tkinter.Label(ventanita, text = resultado) 
        cuad_resultado.pack()

        #Mensaje de despedida
        tex_fin = tkinter.Label(ventanita, text = 'Muchas Gracias por Usar "Calculador Magica", creada por Jorge Arguello')
        tex_fin.pack()

        ventanita.mainloop()

    boton = tkinter.Button(ventana, text = 'Calcular', command= confirm)
    boton.pack()

    ventana.mainloop()
