import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.setWindowTitle("Contador de letras")
        self.setFixedSize(QSize(200,300))
        caja = QVBoxLayout()
        
        self.numeroxtext = QLabel("Numero 1")
        self.numerox = QLineEdit()
        self.numeroytext = QLabel("Numero 2")
        self.numeroy = QLineEdit()
        self.resultadotext = QLabel("El resultado es:")
        self.resultado = QLabel("")
        self.boton = QPushButton("Calcular")
        self.boton2 = QPushButton("Limpiar")

        self.boton.clicked.connect(self.calcular)
        self.boton2.clicked.connect(self.limpiar)
        
        # Se agregan los componentes al layout definido
        caja.addWidget(self.numeroxtext)
        caja.addWidget(self.numerox)
        caja.addWidget(self.numeroytext)
        caja.addWidget(self.numeroy)
        caja.addWidget(self.resultadotext)
        caja.addWidget(self.resultado)
        caja.addWidget(self.boton2)
        caja.addWidget(self.boton)
        
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        
        
        
    #Primera forma de manejar eventos
    def calcular(self):
        suma= int(self.numerox.text()) + int(self.numeroy.text())
        self.resultado.setText(str(suma))
        
    def limpiar(self):
        self.numerox.setText("")
        self.numeroy.setText("")
        self.resultado.setText("")
        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()