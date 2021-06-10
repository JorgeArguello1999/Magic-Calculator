import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel

class Dialogo(QDialog):
    def ___init__ (self):
        QDialog.__init__(self)
        self.resize(300,300)
        self.setWindowsTitle("Cuadro de prueba")
        self.etiqueta = QLabel(self)

class Ventana(QMainWindow):
    def __init__(self):
        dialogo= Dialogo()
        QMainWindow.__init__(self)
        self.resize(300,300)
        self.setWindowTitle("Ventana Principal")
        self.boton = QPushButton(self)
        self.boton.setText("Abrir Cuadro de Dialogo")
        self.boton.resize(200,30)
        self.boton.clicked.connect(self.abrirDialogo)
            
    def abrirDialogo(self):
        self.dialogo.etiqueta.setText("Abriendo el Dialog")
        self.dialogo.exec_()

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()
