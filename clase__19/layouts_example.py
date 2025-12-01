from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Ejemplo de Layouts")

layout = QVBoxLayout()
layout.addWidget(QLabel("Este es un layout vertical"))
layout.addWidget(QPushButton("Botón 1"))
layout.addWidget(QPushButton("Botón 2"))

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
