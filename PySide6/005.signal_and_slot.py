from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget
class Button(QWidget):
    clicked = Signal(Qt.MouseButton)
    
    def mousePressEvent(self, event):
        self.clicked.emit(event.button())