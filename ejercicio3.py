import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.setWindowTitle("Contador de letras")
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()
        
        self.cantidad = QLabel("")
        self.entrada = QLineEdit("Ingresa una palabra")
        self.boton = QPushButton("Contar")
        self.boton.clicked.connect(self.reaccionar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(self.cantidad)
        caja.addWidget(self.entrada)
        caja.addWidget(self.boton)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def reaccionar(self):
        palabra= self.entrada.text()
        self.cantidad.setText("La palabra tiene "+ str(len(palabra))+" letras.")
        self.entrada.setText("")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()