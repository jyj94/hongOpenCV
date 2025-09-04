from common import cv2, np, imgDir

capture =cv2.VideoCapture(imgDir + 'vtest.avi')
if not capture.isOpened(): raise Exception("동영상 파일 개방 안됨")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)
frame_cnt = 0

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break

    blue, green, red = cv2.split(frame)
    frame_cnt += 1

    if 100 <= frame_cnt < 200: cv2.add(blue, 100, blue)
    elif 200 <= frame_cnt < 300: cv2.add(green, 100, green)
    elif 300 <= frame_cnt < 400: cv2.add(red, 100, red)

    frame = cv2.merge([blue, green, red])
    cv2.putText(frame, f'frame : {frame_cnt}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('frame', frame)
capture.release()
cv2.waitKey(0)
