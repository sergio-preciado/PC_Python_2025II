from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
import sys

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Bloc de Notas PyQt5")

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        menu = self.menuBar().addMenu("Archivo")

        abrir = QAction("Abrir", self)
        abrir.triggered.connect(self.abrir_archivo)
        guardar = QAction("Guardar", self)
        guardar.triggered.connect(self.guardar_archivo)

        menu.addAction(abrir)
        menu.addAction(guardar)

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo de texto")
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                self.editor.setText(f.read())

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo")
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())

app = QApplication(sys.argv)
window = Notepad()
window.show()
sys.exit(app.exec_())
