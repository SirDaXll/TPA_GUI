import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit

class Primo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Verificar número primo')
        self.setGeometry(100, 100, 400, 300)

        self.texto = QLabel('Ingresa un número:', self)
        self.texto.move(50, 50)

        self.numero = QLineEdit(self)
        self.numero.setGeometry(50, 80, 200, 25)

        self.boton = QPushButton('Verificar', self)
        self.boton.setGeometry(50, 120, 100, 25)
        self.boton.clicked.connect(self.verificarPrimo)

        self.resultado = QLabel('', self)
        self.resultado.move(50, 160)

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
    window = Primo()
    window.show()
    sys.exit(app.exec())