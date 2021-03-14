import sys
import numpy as np
import cv2


src = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#1.입력영상
#2.오츠에선 그냥 스레시홀드값 0으로 주면 됨
#3. 255로 최대값준다.
#4.바이너리와 오츠로 OR 연산으로 묶어서 해주면된다. 바이너리 안써도 있다고 가정하기때문에 안써도 되긴하다.
# 리턴은 스레시홀드 더블타입과 출력영상으로 리턴한다.
print("otsu's threshold:", th)  # 131
#th값 얼마썼는지 한번 보자.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
