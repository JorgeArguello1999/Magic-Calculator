from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicacion')

        #Creamos un frame que biene a ser el lienzo para la aplicacion
        frame = LabelFrame(self.wind, text = 'Register a new product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #Name de Input
        Label(frame, text = 'name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        #focus en el primer campo del formulario
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Name de Input 2
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price  = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Creando boton
        ttk.Button(frame, text = 'Guardar Datos').grid(row = 3, columnspan = 2, sticky = W + E)

        #Creando una tabla
        #en la propiedad self de 'colunns = 2' hay un "error", no es un error es una mala interpretacion de mi compilador, ese digito esta ok
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Another Name', anchor = CENTER)
        
if __name__ == '__main__':
    window = Tk()
    aplication = Product(window)
    window.mainloop()
