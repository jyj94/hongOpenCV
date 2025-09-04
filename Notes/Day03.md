# 비디오 처리
## 리눅스에서 카메라 설정
리눅스에서 사용하려면 드라이버를 직접 설정해야 하는 경우가 있음

WSL의 경우, 장치의 연결을 윈도우에서 WSL로 넘겨줘야함

윈도우 -TCP/IP-> WSL

### 리눅스 설정
1. 파워쉘 관리자 권한으로 실행
2. <code>winget install --interactive --exact dorssel.usbipd-win</code> 실행
3. USB 리스트 확인 <code>usbipd list</code>
4. USB 장치 바인드 <code>usbipd bind --busid 1-6</code>
5. USB 장치 attach <code>usbipd attach --wsl --busid 1-6</code>
6. <code>usbipd list</code>를 입력하여 장치의 상태가 Attached인지 확인
7. 리늑스에 <code>/dev/video0</code>, <code>/dev/video1</code>이 생성되거나 <code>lsusb</code> 명령어를 사용하여 장치 연결 확인

## numpy array 다루기
🔶 1. 배열의 기본 구조 이해
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


이건 3x3 2D 배열입니다. 여기서 중요한 건:

a.shape → (3, 3)

a[0] → [1, 2, 3]

a[1, 2] → 6

🔶 2. 슬라이싱과 인덱싱
a[:, 1]       # 모든 행의 두 번째 열 → [2, 5, 8]
a[1, :]       # 두 번째 행 전체 → [4, 5, 6]
a[0:2, 0:2]   # 왼쪽 위 2x2 → [[1, 2], [4, 5]]


: → 전체

start:stop → 범위 (stop은 포함 안 됨)

🔶 3. 차원 추가 / 제거
a = np.array([1, 2, 3])

a.shape                  # (3,)
a[np.newaxis, :]         # (1, 3)
a[:, np.newaxis]         # (3, 1)
np.expand_dims(a, axis=0)  # (1, 3)
np.squeeze()             # 불필요한 차원 제거

🔶 4. 배열 합치기
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.concatenate([a, b], axis=0)  # 행 방향 합치기 (4x2)
np.concatenate([a, b], axis=1)  # 열 방향 합치기 (2x4)

np.stack([a, b], axis=0)  # 새로운 차원 추가 (2, 2, 2)

🔶 5. 배열 복사
b = a.copy()  # 깊은 복사
b = a         # 얕은 복사 (같은 메모리 참조)

🔶 6. OpenCV 이미지 → NumPy 배열
import cv2

img = cv2.imread('image.jpg')  # BGR 이미지, shape: (H, W, 3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # shape: (H, W)

roi = img[100:200, 150:250]  # 이미지의 특정 영역 잘라내기 (ROI)
img[0:100, 0:100] = 0        # 이미지 왼쪽 위를 검정색으로 덮기

🔶 7. 마스크나 조건 필터링
a = np.array([[1, 2], [3, 4]])

mask = a > 2          # [[False, False], [True, True]]
a[mask]               # [3, 4]

🔶 8. 실전 응용 예: 이미지에 사각형 그리기
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)
cv2.imshow("rect", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

정리: 배열 자유자재로 다루기 위한 핵심
목표	사용 함수 / 문법
슬라이싱/인덱싱	a[i:j, k:l], a[:, 1]
차원 조작	reshape(), expand_dims(), squeeze()
합치기	concatenate(), stack()
복사/참조	copy(), 직접 대입
이미지 조작	cv2.imread(), cv2.cvtColor()
조건 필터링	a[a > 5], 마스크 배열