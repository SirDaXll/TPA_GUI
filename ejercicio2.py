import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Voltear(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        # Crear los widgets
        self.palabra = QLineEdit()
        self.alreves = QLabel()

        voltear = QPushButton('Voltear la palabra')
        voltear.clicked.connect(self.reverse_word)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.palabra)
        vbox.addWidget(voltear)
        vbox.addWidget(self.alreves)

        # Set layout
        self.setLayout(vbox)

        # Set propiedades de la ventana
        self.setWindowTitle('Volteador de palabras')
        self.setGeometry(100, 100, 300, 200)
        self.show()

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
    ex = Voltear()
    sys.exit(app.exec())