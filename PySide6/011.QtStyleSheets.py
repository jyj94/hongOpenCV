import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placehoder text")
    w.setAlignment(Qt.AlignCenter)
    '''
    w.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """)
    '''
    w.show()
    w.setObjectName('title')
    with open('QtSide6\style.qss', 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)
    
    sys.exit(app.exec())