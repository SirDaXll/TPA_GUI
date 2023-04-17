import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.setWindowTitle("Contador de letras")
        #self.setFixedSize(QSize(200,300))
        caja = QVBoxLayout()
        
        self.nombretext = QLabel("Ingrese el nombre")
        self.nombre = QLineEdit()
        self.apellidotext = QLabel("Ingrese el Apellido")
        self.apellido = QLineEdit()
        self.boton = QPushButton("Ingresar")
        self.boton2 = QPushButton("Limpiar")

        self.boton.clicked.connect(self.lista)
        self.boton2.clicked.connect(self.limpiar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(self.nombretext)
        caja.addWidget(self.nombre)
        caja.addWidget(self.apellidotext)
        caja.addWidget(self.apellido)
        caja.addWidget(self.boton2)
        caja.addWidget(self.boton)
        
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

        #creamos la lista para usar
        self.lista= []
        
        
        
    #Primera forma de manejar eventos
    def lista(self):
        #traemos los atributos
        nombre = self.nombre.text()
        apellido = self.nombre.text()

        persona = Persona(nombre, apellido)

        self.lista.append(persona)


        
    def limpiar(self):
        self.nombre.setText("")
        self.apellido.setText("")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()