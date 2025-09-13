import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)  # 애플리케이션 인스턴스 생성. sys.argv를 통해 커맨드라인 인자를 전달
label = QLabel("<font color=red size=40>Hello World!</font>")  # QLabel 위젯 생성, 표시할 텍스트 설정
label.show()  # 위젯을 화면에 표시
app.exec()  # 이벤트 루프 시작. 앱이 사용자 입력을 처리하도록 함