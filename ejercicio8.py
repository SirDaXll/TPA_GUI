import sys
import re
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class Correo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Validador de correo electrónico')
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.texto = QLabel('Ingresa un correo electrónico:')
        self.correo = QLineEdit(self)

        self.boton = QPushButton('Validar', self)
        self.boton.clicked.connect(self.validar)

        self.resultado = QLabel('', self)

        caja.addWidget(self.texto)
        caja.addWidget(self.correo)
        caja.addWidget(self.boton)
        caja.addWidget(self.resultado)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def validar(self):
        email = self.correo.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.resultado.setText('El correo electrónico es válido')
        else:
            self.resultado.setText('El correo electrónico no es válido')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Correo()
    ventana.show()
    sys.exit(app.exec())