"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
"""

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
import sys

app = QApplication(sys.argv)

ui_file_name = "QtSide6\mainwindow.ui"
ui_file = QFile(ui_file_name)
if not ui_file.open(QIODevice.ReadOnly):
    print(f'Cannot open {ui_file_name}: {ui_file.errorString()}')
    sys.exit(-1)

loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()
if not window:
    print(loader.errorString())
    sys.exit(-1)

window.show()
sys.exit(app.exec())