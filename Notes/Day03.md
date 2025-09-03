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

## 비트 연산으로 마스킹 하기
