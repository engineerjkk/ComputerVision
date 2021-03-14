import sys
import cv2


# 비디오 파일 열기
cap = cv2.VideoCapture()
cap.open(0)# -> 카메라 기본 카메라를 오픈하겠다.
#cap = cv2.VideoCapture('video2.mp4') #해주면 파일을 불러온다. 
#cap=cv2.VideoCapture(0) 을 해줘도 똑같다.
if not cap.isOpened(): #카메라가 열리지 않았으면 실행하고 종료해라.
    print("Video open failed!")
    sys.exit()
#비디로 프레임 임의로 설정해주기
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)


# 비디오 프레임 크기, 전체 프레임수, FPS 등 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
#프레임의 크기를 알고싶을때
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS:', fps)

delay = round(1000 / fps)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()#카메라로부터 한프레임씩 받아옴
#read함수가 현재프레임을 그대로 받아오는게 아니라
#현재프레임을 제대로받아왔는지 확인하는 true false도 받아오므로(Bool 타입 함수),
#인자는 두개해주고 ret에 true false를 받는다.
    if not ret:
        break
#제대로 못받아왔으면 break된다.
#정상적으로 받아왔는지 확인하는 불타입 변수
#이미지 파일의 경우 마지막 프레임이 지나면 ret에 false가 되어서 break가 걸리고 빠져나오게 된다.


    #inversed = ~frame  # 반전
    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    #cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27: #ESC를 누르면 해제
        break

cap.release() #캡을 릴리즈한다.
cv2.destroyAllWindows() #모든창을 닫는다.
