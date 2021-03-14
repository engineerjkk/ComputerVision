import sys
import numpy as np
import cv2


src = cv2.imread('keyboard.bmp', cv2.IMREAD_GRAYSCALE)
#이미지 그레이스케일 레벨로 받음
if src is None:#만약 이미지가 없으면 실패 출력
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
#이진화를 자동으로 할거니 0~255로 주고 오츠기법을 사용한다.,바이너리 생략해도무방 원래는 cv2.THRESH_BINARY|cv2.THRESH_OTSU
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
#전체객체개수,labels,stats,centroids 기본용어를 사용하자. stats와 centroids를 통해 어느객체가 어느위치에 어떻게 놓여있는지를 알 수 있다.
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
#src가 그레이스케일이라 빨간색으로 사각형으로 그릴수있도록 dst를 컬러로 바꾸어준다.
for i in range(1, cnt):#배경은 제외할거니 1부터 시작한다.
    (x, y, w, h, area) = stats[i] 
    #i번째 행이 x,y,w,h,a(픽셀개수)가 차례대로 들어간다.

    if area < 20:
        continue
    #오프닝으로 노이즈를 제거해도되지만, 검출한 픽셀값인 area값이 20보다 작으면 무시하는 방법을 사용한다.
    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))
    #그러면 rectangle함수에다가 x,y,w,h 그대로 넣으면된다.
    #세번째 인자는 컬러값 빨간색으로 준다. 

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
