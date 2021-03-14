import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#round는 반올림 함수 
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) #스펙에 맞는 프레임 저장
#fps=30 이런식으로 강제로 30 줘도됨.

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
#
delay = round(1000 / fps)
#한프레임과 그다음프레임 시간값을 계산


out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))
#output.avi이름으로 저장하고, 압    축방식은 fourcc DIVX로 저장한다. 마지막은 default로했기때문에 컬러로 저장한다. 

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame
    edge=cv2.Canny(frame,50,150)

    #out.write(inversed)

    cv2.imshow('frame', frame)
    cv2.imshow('edge',edge)
    #edge영상은 그레이스케일이라서 저장이안된다. 따라서 컬러영상으로 변환해서 저장해야한다.
    edge_color=cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)
    #그레이스케일 이비지를 BGR로 변환해라
    out.write(edge_color)
    #cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
