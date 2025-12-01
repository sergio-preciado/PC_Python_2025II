from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menús y Diálogos")

        menu = self.menuBar().addMenu("Archivo")
        abrir = QAction("Abrir archivo", self)
        abrir.triggered.connect(self.abrir_archivo)
        menu.addAction(abrir)

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Selecciona un archivo")
        if ruta:
            print("Seleccionado:", ruta)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
