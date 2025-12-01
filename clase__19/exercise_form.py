from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
import sys

def enviar():
    nombre = entrada.text()
    label_result.setText(f"Hola, {nombre}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Ejercicio: Formulario Simple")

layout = QVBoxLayout()
entrada = QLineEdit()
entrada.setPlaceholderText("Escribe tu nombre")
boton = QPushButton("Enviar")
boton.clicked.connect(enviar)
label_result = QLabel("")

layout.addWidget(entrada)
layout.addWidget(boton)
layout.addWidget(label_result)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
