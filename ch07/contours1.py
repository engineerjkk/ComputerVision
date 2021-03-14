import sys
import random
import numpy as np
import cv2


src = cv2.imread('contours.bmp', cv2.IMREAD_GRAYSCALE)
#이미 이진영상이라. 따로 이진화를 안해도 된다.
if src is None:
    print('Image load failed!')
    sys.exit()

contours, hier = cv2.findContours(src, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#2 level로 계층구조를 만들겠다.
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
#출력영상을 컬러로 해야해서 컬러로 변환해준다.
idx = 0
#첫번째 외곽선을 0번으로 지정
while idx >= 0:
    c = (random.randint(0, 255), random.randint(0, 255),
 random.randint(0, 255))
 #BGR을 랜덤하게 찾기 위해서 컬러값을 만든다.
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8,hier)
    #drawContours 함수로 외곽선을 그린다.
    #c : 임의의 컬럭밧
    #2 : 두께는 2
    #Line_8 라인 타입

    idx = hier[0, idx, 0]
    #인덱스를 업데이트 하는 방식
    #hierachy 가 1,N,4의 shape을 갖는다.
    #무조건 첫번째꺼는 0을 준다.
    #4자리에 0을 주면 next로 넘어가는 것이다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
