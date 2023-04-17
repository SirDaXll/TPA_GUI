import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class Primo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Verificar número primo')
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.texto = QLabel('Ingresa un número:')
        self.numero = QLineEdit(self)

        self.boton = QPushButton('Verificar', self)
        self.boton.clicked.connect(self.verificarPrimo)

        self.resultado = QLabel('', self)

        caja.addWidget(self.texto)
        caja.addWidget(self.numero)
        caja.addWidget(self.boton)
        caja.addWidget(self.resultado)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def verificarPrimo(self):
        num = int(self.numero.text())
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    self.resultado.setText(f'{num} no es un número primo')
                    break
            else:
                self.resultado.setText(f'{num} es un número primo')
        else:
            self.resultado.setText(f'{num} no es un número primo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Primo()
    ventana.show()
    sys.exit(app.exec())