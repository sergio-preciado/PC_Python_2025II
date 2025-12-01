from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

contador = 0

def incrementar():
    global contador
    contador += 1
    label.setText(f"Contador: {contador}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Ejercicio: Contador")

layout = QVBoxLayout()
label = QLabel("Contador: 0")
button = QPushButton("Incrementar")
button.clicked.connect(incrementar)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
