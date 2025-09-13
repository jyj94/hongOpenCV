"""
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)
        
    def greetings(self):
        print(f'hello {self.edit.text()}')
        
if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    sys.exit(app.exec())
"""

import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle = "My Form"
        
        self.edit = QLineEdit("Write you name here")
        self.button = QPushButton("Sumit")
        
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
        self.button.clicked.connect(self.method1)
        self.show()
        
    @Slot()    
    def method1(self):
        print(f'hello {self.edit.text()}')
        

app = QApplication()
form = Form()
sys.exit(app.exec())