import sys, cv2, numpy as np
from PySide6.QtCore import QFile, Slot, Qt, QTimer
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QGraphicsView, QPushButton, QComboBox, QCheckBox
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QMessageBox

class Player():
    def __init__(self):
        #윈도우 초기화 및 UI 파일 불러오기
        self.app = QApplication([])
        
        ui_file = QFile("MyApp02/main_window.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        del loader
        
        #위젯 초기화
        self.videoFileButton = self.window.findChild(QPushButton, "videoFileButton")
        self.videoFileButton.clicked.connect(self.videoFileDialog)
        self.playPauseButton = self.window.findChild(QPushButton, "playPauseButton")
        self.playPauseButton.clicked.connect(self.playAndPause)
        self.speedComboBox = self.window.findChild(QComboBox, "speedComboBox")
        self.color2GrayCheckBox = self.window.findChild(QCheckBox, "color2GrayCheckBox")
        
        self.graphicsView = self.window.findChild(QGraphicsView, "graphicsView")
        self.graphicsScene = QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)
        self.pixmapItem = QGraphicsPixmapItem()
        self.graphicsScene.addItem(self.pixmapItem)
        
        #비디오 관련 변수
        self.videoCap = None
        self.fps = 0
        self.currentFrame = 0
        self.MaximumFrame = 0
        self.isPlay = False
        
        #타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrame)
        
        self.window.show()
        
    def run(self):
        sys.exit(self.app.exec())
        
    @Slot()
    def videoFileDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.window,
            "Select an video file",
            "D:/Apex/Apex-Clip",
            "Videos (*.mp4 *.MP4 *.mkv *.MKV)"
        )
        
        if filePath:
            self.videoCap = cv2.VideoCapture(filePath)
            if not self.videoCap.isOpened():
                QMessageBox.warning(self.window, "에러", "비디오를 열 수 없습니다.")
                return

        #비디오 변수 초기화
        self.fps = self.videoCap.get(cv2.CAP_PROP_FPS)
        self.currentFrame = -1
        self.MaximumFrame = self.videoCap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f'selected file: {filePath}')
        print(f"해상도: {self.videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{self.videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        print(f"FPS: {self.videoCap.get(cv2.CAP_PROP_FPS)}")
        print(f"총 프레임: {self.videoCap.get(cv2.CAP_PROP_FRAME_COUNT)}")
        
        self.nextFrame()
        self.graphicsScene.setSceneRect(self.pixmapItem.boundingRect())
        self.graphicsView.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
    
    def replaceViewer(self, frame):
        #체크박스 여부에 따라 색공간 변경
        if self.color2GrayCheckBox.isChecked():
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        else:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        qimg = QImage(rgb_frame.data, w, h, w * ch, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        
        self.pixmapItem.setPixmap(pixmap)
        
    def nextFrame(self):
        ret, frame = self.videoCap.read()
        self.currentFrame += 1
        if self.currentFrame >= self.MaximumFrame:
            self.videoCap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.currentFrame = -1
        if ret:
            self.replaceViewer(frame)
        
    @Slot()    
    def playAndPause(self):
        if self.isPlay:
            self.timer.stop()
            self.isPlay = False
            return
        if self.videoCap is None:
            return
        if self.timer.isActive():
            self.timer.stop()
            
        speed_map = {"x1.0": 1.0, "x1.5": 1.5, "x2.0": 2.0}
        selected_text = self.speedComboBox.currentText()  # 예: "x1.5"
        multiple = speed_map.get(selected_text, 1.0)  
        interval = int(1000 / self.fps / multiple)
        print(interval)
        self.timer.start(interval)
        self.isPlay = True
        
        
    

player = Player()
player.run()