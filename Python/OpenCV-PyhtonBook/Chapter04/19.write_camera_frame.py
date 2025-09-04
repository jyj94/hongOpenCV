from common import cv2, np, imgDir

capture = cv2.VideoCapture(imgDir + 'vtest.avi') # 카메라 입력 시작
if capture.isOpened() == False: # 연결 확인
    raise Exception("카메라 연결 안됨")


fps = 29.97
delay = round(1000 / fps)
size = (640, 360)


print(f"width x height : {size}")
print(f"delay : {size}ms")
print(f"fps : {fps}")

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 지정
writer = cv2.VideoWriter(imgDir + 'output.avi', fourcc, fps, size)
if not writer.isOpened(): raise Exception("can't open video writer")

while True:
    ret, frame = capture.read()
    if not ret: break

    frame_resized = cv2.resize(frame, size)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

    writer.write(frame_resized)
    
writer.release()
capture.release()