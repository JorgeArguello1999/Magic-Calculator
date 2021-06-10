from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import *

class Product:
    def __init__(self, window):

        self.wind = window
        self.wind.title('Calculadora Magica')

        #Creamos el lienzo
        frame = LabelFrame(self.wind, text = 'Calculadora Magica')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Creamos el boton
        ttk.Button(frame, text = 'Calculadora de la Temperatura').grid(row = 1, columnspan = 1, sticky = W+E)
        ttk.Button(frame, text = 'Calculadora de Calorias').grid(row = 3, columnspan = 1, sticky = W+E)
        ttk.Button(frame, text = 'Calculadora de Porcentajes').grid(row = 5, columnspan = 1, sticky = W+E)
        ttk.Button(frame, text = 'Peso en Otro Planeta').grid(row = 7, columnspan = 1, sticky = W+E)

        imagen = Image("Transformaciones.png")


if __name__ == '__main__':
    window = Tk()
    aplication = Product(window)
    window.mainloop()
