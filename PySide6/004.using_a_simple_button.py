"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("button clicked, Hello!")
    

app = QApplication(sys.argv)

button = QPushButton("Click me")
button.clicked.connect(say_hello)

button.show()
app.exec()
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Slot


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello App")

button = QPushButton("click me")
label = QLabel("")

@Slot()
def say_hello():
    label.setText(label.text() + "Hello\n")  # 수정: text() 호출 + setText() 사용

button.clicked.connect(say_hello)

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)

window.show()
app.exec() 