import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class Voltear(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Volteador de palabras')
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.texto = QLabel('Ingresa una palabra:')
        self.palabra = QLineEdit(self)
        self.alreves = QLabel(self)

        self.voltear = QPushButton('Voltear la palabra', self)
        self.voltear.clicked.connect(self.reverse_word)

        self.texto1 = QLabel('La palabra al revés es:')

        caja.addWidget(self.texto)
        caja.addWidget(self.palabra)
        caja.addWidget(self.voltear)
        caja.addWidget(self.texto1)
        caja.addWidget(self.alreves)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)


    def reverse_word(self):
        # Obtener la palabra ingresada por el usuario
        word = self.palabra.text()

        # Voltear la palabra
        reversed_word = word[::-1]

        # Mostrar la palabra volteada en el QLabel
        self.alreves.setText(reversed_word)

if __name__ == '__main__':
    # Inicializar la aplicación
    app = QApplication(sys.argv)
    window = Voltear()
    window.show()
    sys.exit(app.exec())