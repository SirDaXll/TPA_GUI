import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class Fruta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lista de frutas')
        caja = QVBoxLayout()

        self.texto = QLabel('Ingresa una fruta a la lista:')
        self.fruta = QLineEdit(self)

        self.boton = QPushButton('Agregar')

        self.boton.clicked.connect(self.agregar)

        self.lista = QLabel("Lista de frutas:\n")

        caja.addWidget(self.texto)
        caja.addWidget(self.fruta)
        caja.addWidget(self.boton)
        caja.addWidget(self.lista)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def agregar(self):
        item = self.fruta.text()

        self.lista.setText(self.lista.text() + item + "\n")

        self.fruta.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Fruta()
    window.show()
    sys.exit(app.exec())