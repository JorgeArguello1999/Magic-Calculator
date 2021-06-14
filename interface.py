import tkinter
from tkinter import Label
from tkinter import Image, ttk

#Importamos los modulos
import C_temperatura
import C_calorias
import C_porcentaje

ventana = tkinter.Tk()
ventana.geometry('500x300')

#Nombre de la ventana
ventana.title('Calculadora Magica')

#Encabezado de la aplicacion
texto = tkinter.Label(ventana, text = 'Calculadora Magica')
texto.pack()

#Intenton de colocar una imagen en el menu principal
imagen = tkinter.PhotoImage(file = 'Banner.png')
Label(ventana, image = imagen, bd = 0).pack(side = 'left')

def eleccion(numero):
    print(numero)
    if numero == 1:
        print("Calculadora de Temperatura")

        #Llammos al modulo de C_temperatura
        C_temperatura.ventanita()
        
    if numero == 2:
        print("Calculadora de Calorias")

        #Llamamos al modulo de C_calorias
        C_calorias.ventana()

    if numero == 3:
        print ("Calculadora de Porcentaje")
        
        #Llamamos al modulo de C_porcentaje 
        C_porcentaje.ventana()

boton1 = tkinter.Button(ventana, text = 'Calculadora de Temperatura', command = lambda: eleccion(1))
boton1.pack()

boton2 = tkinter.Button(ventana, text = 'Calculadora de Calorias', command = lambda: eleccion(2))
boton2.pack()

boton3 = tkinter.Button(ventana, text = 'Calculadora de Porcentaje', command = lambda: eleccion(3))
boton3.pack()

ventana.mainloop()
