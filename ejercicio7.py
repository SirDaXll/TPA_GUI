import sys
import random

from PyQt6.QtGui import QColor
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.setWindowTitle("Cambia Color")
        self.setFixedSize(QSize(400,200))
        
        #Generamos un boton y le asignamos que hacer cuando suceda el evento(click)
        self.boton = QPushButton("Presioname para fiesta")
        self.boton.clicked.connect(self.cambiarColor)
        
        self.setCentralWidget(self.boton)
        
    #Primera forma de manejar eventos
    def cambiarColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)

        estilo = f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});"

        self.boton.setStyleSheet(estilo)
# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()