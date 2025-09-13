import sys
import numpy as np, cv2
from PySide6.QtWidgets import QApplication, QPushButton, QSlider, QCheckBox, QGraphicsView
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QTextEdit, QMessageBox
from PySide6.QtGui import QImage, QPixmap

class MainWindow():
    def __init__(self):        
        #이미지 파일, 매트릭스
        self.file_path = None
        self.originalImg = None
        self.resultImg = None
        
        #윈도우 초기화 및 UI 파일 불러오기
        self.app = QApplication([])
        self.ui_file = QFile("MyApp/main_ui.ui")
        self.ui_file.open(QFile.ReadOnly)
        self.loader = QUiLoader()
        self.window = self.loader.load(self.ui_file)
        self.ui_file.close()
        del self.loader
        
        #버튼 초기화
        self.readFileButton = self.window.findChild(QPushButton, "readFileButton")
        self.resetButton = self.window.findChild(QPushButton, "resetButton")
        self.button01 = self.window.findChild(QPushButton, "button01")
        self.button02 = self.window.findChild(QPushButton, "button02")

        #슬라이더 초기화
        self.function01Slider = self.window.findChild(QSlider, "function01Slider")
        self.function02Slider = self.window.findChild(QSlider, "function02Slider")
        self.function03Slider = self.window.findChild(QSlider, "function03Slider")

        #체크박스 초기화
        self.function05CheckBox = self.window.findChild(QCheckBox, "function05CheckBox")
        self.function06CheckBox = self.window.findChild(QCheckBox, "function06CheckBox")
        self.function07CheckBox = self.window.findChild(QCheckBox, "function07CheckBox")
        
        #텍스트 에디터 초기화
        self.blurStrength = self.window.findChild(QTextEdit, "blurStrength")
        
        #버튼 동작 바인드
        self.readFileButton.clicked.connect(self.openFileDialog)
        self.resetButton.clicked.connect(self.resetFuction)
        self.button01.clicked.connect(self.buttonFunction1)
        self.button02.clicked.connect(self.buttonFunction2)
        
        #슬라이더 동작 바인드
        self.function01Slider.valueChanged.connect(self.updateResultimg)
        self.function02Slider.valueChanged.connect(self.updateResultimg)
        self.function03Slider.valueChanged.connect(self.updateResultimg) 
        
        #체크박스 동작 바인드
        self.function05CheckBox.toggled.connect(self.updateResultimg)
        self.function06CheckBox.toggled.connect(lambda checked: print(f"check box 02: {checked} / {type(checked)}"))
        self.function07CheckBox.toggled.connect(lambda checked: print(f"check box 03: {checked} / {type(checked)}"))
        
        #그래픽뷰어 초기화
        self.originalViewer = self.window.findChild(QGraphicsView, "originalViewer")
        self.resultViewer = self.window.findChild(QGraphicsView, "resultViewer")
        self.originalScene = QGraphicsScene()
        self.resultScene = QGraphicsScene()

        self.originalViewer.setScene(self.originalScene)
        self.resultViewer.setScene(self.resultScene)
        
    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
    
    def changeViewer(self, viewer, img):
        #타입 체크
        if not isinstance(viewer, QGraphicsView):
            raise TypeError("viewer Type is not QGraphicsView")
        if not isinstance(img, np.ndarray):
            raise TypeError("image Type is not numpy.array")

        # numpy -> QPixmap 변환
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        qimg = QImage(rgb_image.data, w, h, w*3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        scene = viewer.scene()
        
        if scene.items():  # 기존 아이템이 있으면 재사용
            item = scene.items()[0]  
            if isinstance(item, QGraphicsPixmapItem):
                item.setPixmap(pixmap)
        else:  # 없으면 새 아이템 생성
            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
        
        scene.setSceneRect(item.boundingRect())
        viewer.fitInView(item, Qt.KeepAspectRatio)
        
    def openFileDialog(self):
        # 파일 열기 다이얼로그
        self.file_path, _ = QFileDialog.getOpenFileName(
            self.window,                   # 부모 윈도우
            "Select an image",    # 다이얼로그 제목
            "",                            # 초기 경로
            "Images (*.png *.jpg *.bmp)"  # 필터
        )
        
        if self.file_path:  # 선택한 파일이 있으면
            print("Selected file:", self.file_path)
            # 예시: 이미지라면 QGraphicsView에 표시
            if any(self.file_path.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".bmp", ".JPG", ".JPEG", ".PNG", ".BMP"]):
                img = cv2.imread(self.file_path)
                self.originalImg = img
                self.resultImg = self.originalImg.copy()
                self.changeViewer(self.originalViewer, self.originalImg)
                self.changeViewer(self.resultViewer, self.originalImg)
                self.resetFuction()
                
    def openMessageBox(self, icon, title = "", text = "", type = 0):
        #타입 0 : 예, 타입 1 : 예/아니오
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        
        if type == 0:
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        else:
            msg.setStandardButtons(QMessageBox.Cancel)
            
        ret = msg.exec()
        
        if ret == QMessageBox.Ok:
            print(QMessageBox.Ok)
        else:
            print(QMessageBox.Cancel)
            

    def resetFuction(self):
        #슬라이드 초기화
        self.function01Slider.setValue(0)
        self.function02Slider.setValue(0)
        self.function03Slider.setValue(0)
        
        self.function05CheckBox.setChecked(False)
        self.function06CheckBox.setChecked(False)
        self.function07CheckBox.setChecked(False)
        
        self.blurStrength.setText("")

        if self.originalImg is not None:
            self.resultImg = self.originalImg.copy()
            self.changeViewer(self.resultViewer, self.resultImg)
        
    def buttonFunction1(self):
        pass
    
    def buttonFunction2(self):
        pass

    def updateResultimg(self):
        if self.originalImg is None:
            self.openMessageBox(QMessageBox.Information, "이미지 파일 불러오지 않음", "Image File 버튼을 눌러 이미지 파일을 불러오세요.", 1)
            self.resetFuction()
            return
                
        self.resultImg = self.originalImg.copy()
        
        self.resultImg[:, :, 2] = cv2.add(self.resultImg[:, :, 2], self.function01Slider.value())
        self.resultImg[:, :, 1] = cv2.add(self.resultImg[:, :, 1], self.function02Slider.value())
        self.resultImg[:, :, 0] = cv2.add(self.resultImg[:, :, 0], self.function03Slider.value())
        
        if self.function05CheckBox.isChecked():
            if self.blurStrength.toPlainText() != "":
                self.resultImg = cv2.GaussianBlur(self.resultImg, (31, 31), int(self.blurStrength.toPlainText()))
            else:
                self.openMessageBox(QMessageBox.Warning, "세기 입력 안함", "블러의 세기를 입력하세요.\n", 1)
                self.function05CheckBox.setChecked(False)

        self.changeViewer(self.resultViewer, self.resultImg)
        
if __name__ == "__main__":
    mainApp = MainWindow()
    mainApp.run()


