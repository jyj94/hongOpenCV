import cv2

def put_string(frame, text, pt, value, color=(120,200,90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, text, pt, font, 0.7, color, 2, cv2.LINE_AA)

capture = cv2.VideoCapture(0) # 카메라 입력 시작
if capture.isOpened() == False: # 연결 확인
    raise Exception("카메라 연결 안됨")

#카메라 정보 출력
print("width: ", capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height: ", capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("exposure: ", capture.get(cv2.CAP_PROP_EXPOSURE))
print("brightness: ", capture.get(cv2.CAP_PROP_BRIGHTNESS))
print("fps: ", capture.get(cv2.CAP_PROP_FPS))

#이미지 입력 루프
while True:
    ret, frame = capture.read()
    #루프 정지 조건
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    #노출값 영상에 표시
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, "EXPOS: ", (10, 40), exposure)

    #UI 표시
    
    title = "View Frame from Camera"
    cv2.imshow(title, frame)

#카메라 연결 종료
capture.release()
