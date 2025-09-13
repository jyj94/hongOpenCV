import sys, cv2, numpy as np, time
from PySide6.QtCore import Qt, QThread, Signal, QFile
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtWidgets import QPushButton

class CameraThread(QThread):
    frameReady = Signal(object)
    
    def __init__(self, cap):
        super().__init__()
        self.cap = cap
        self.running = True
    
    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frameReady.emit(frame)

class Window():
    def __init__(self):
        
        self.app = QApplication([])
        self.cap = cv2.VideoCapture(0)
        self.isPlay = False
        
        ui_file = QFile("MyApp04/mainWindow.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        del loader
        
        self.connectButton = self.window.findChild(QPushButton, "connectButton")
        self.connectButton.clicked.connect(self.buttonClick)
        
        self.graphicsView = self.window.findChild(QGraphicsView, "graphicsView")
        self.graphicsScene = QGraphicsScene()
        self.graphicsItem = QGraphicsPixmapItem()
        self.graphicsScene.addItem(self.graphicsItem)
        self.graphicsView.setScene(self.graphicsScene)
        
        self.cameraThread = CameraThread(self.cap)
        self.cameraThread.frameReady.connect(self.changeFrame)
        
    def buttonClick(self):
        self.isPlay = not self.isPlay
        if self.isPlay:
            # 버튼 클릭 시마다 새 스레드 생성
            self.cameraThread.start()
            self.cameraThread.running = True
        else:
            self.cameraThread.running = False
        
    def playingVideo(self):
        while self.isPlay:
            ret, frame = self.cap.read()
            self.changeFrame(frame)
            time.sleep(0.01)
            
    def changeFrame(self, frame):
        cv2.flip(frame, 1, frame)
        
        # 영상 알고리즘 위치
        dst = np.array([[0,0],[2,0],[2,2],[0,2]], dtype=np.float32)
        frame = cv2.perspectiveTransform(frame, dst)
        
        
        
        frame = cv2.putText(
            frame, 
            f'fps : {self.cap.get(cv2.CAP_PROP_FPS)}', 
            (50, 50), 
            cv2.FONT_HERSHEY_SIMPLEX,    
            1,                            
            (0, 255, 0),                  
            2)
        
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        h, w, ch = rgbFrame.shape
        qimg = QImage(rgbFrame.data, w, h, w * ch, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        
        self.graphicsItem.setPixmap(pixmap)
        self.graphicsView.fitInView(self.graphicsItem, Qt.KeepAspectRatio)
    
    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
    
app = Window()

app.run()