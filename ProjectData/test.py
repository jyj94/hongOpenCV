import numpy as np
import cv2

class sprite(self):
    def __init__(self):
        self.pos = (0, 0)
        self.width = 0
        self.height = 0
        self.imageData = np.zeros((0,0,3), np.uint8)

    def blit(self, inputimage):
        pass

    def draw(self):
        pass
    
    def update(self):
        pass

    def setSprite(self, inputimage, inputPos=(0,0)):
        self.pos = inputPos
        self.imageData = inputimage
        self.height, self.width = inputimage.shape[:2]

class textSprite(sprite):
    pass

class logoSprite(sprite):
    pass

class mainDraw(self):
    def __init__(self):
        self.canvas = np.zeros((1000, 1000, 3), np.uint8)
        self.mousePos = (0, 0)
        self.bgrValue

        self.showCanvas()

    def drawSprite(self, sprite):
        x, y = sprite.pos
        h, w = sprite.height, sprite.width
        if h > 0 and w > 0:
            self.canvas[y:y+h, x:x+w] = sprite.imageData
    def run(self):
        pass

    def update(self):
        self.showCanvas()
        
        
    def showCanvas(self):
        cv2.imshow('canvas', self.canvas)

def main():
    mainDraw = mainDraw()
    mainDraw.run()

if __name__ == "__main__":
    main()