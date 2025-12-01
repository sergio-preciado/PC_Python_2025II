from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

def on_click():
    label.setText("¡Botón presionado!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Señales y Slots")

layout = QVBoxLayout()

label = QLabel("Presiona el botón")
button = QPushButton("Haz clic")
button.clicked.connect(on_click)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
