import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QMessageBox, QHBoxLayout
)

class Cajero(QWidget):
    def __init__(self):
        super().__init__()
        self.saldo = 100000  # saldo inicial
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cajero Automático PyQt5")

        self.label = QLabel(f"Saldo actual: ${self.saldo}")
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ingrese valor")

        btn_ret = QPushButton("Retirar")
        btn_dep = QPushButton("Depositar")
        btn_cons = QPushButton("Consultar saldo")

        btn_ret.clicked.connect(self.retirar)
        btn_dep.clicked.connect(self.depositar)
        btn_cons.clicked.connect(self.consultar)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        h = QHBoxLayout()
        h.addWidget(btn_ret)
        h.addWidget(btn_dep)
        layout.addLayout(h)

        layout.addWidget(btn_cons)

        self.setLayout(layout)

    def retirar(self):
        try:
            val = int(self.input.text())
            if val <= 0:
                raise ValueError
            if val > self.saldo:
                QMessageBox.warning(self, "Error", "Fondos insuficientes")
            else:
                self.saldo -= val
                self.label.setText(f"Saldo actual: ${self.saldo}")
                QMessageBox.information(self, "OK", "Retiro exitoso")
        except:
            QMessageBox.warning(self, "Error", "Ingrese un número válido")

    def depositar(self):
        try:
            val = int(self.input.text())
            if val <= 0:
                raise ValueError
            self.saldo += val
            self.label.setText(f"Saldo actual: ${self.saldo}")
            QMessageBox.information(self, "OK", "Depósito exitoso")
        except:
            QMessageBox.warning(self, "Error", "Ingrese un número válido")

    def consultar(self):
        QMessageBox.information(self, "Saldo", f"Su saldo es: ${self.saldo}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Cajero()
    win.show()
    sys.exit(app.exec_())
