from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Widgets Básicos")

layout = QVBoxLayout()
label = QLabel("Escribe tu nombre:")
input_box = QLineEdit()

layout.addWidget(label)
layout.addWidget(input_box)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
