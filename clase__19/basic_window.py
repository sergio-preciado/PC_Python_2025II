from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Ventana Básica PyQt5")
window.resize(400, 300)
window.show()

sys.exit(app.exec_())
