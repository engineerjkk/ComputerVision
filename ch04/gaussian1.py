import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

#가우시안필터
dst = cv2.GaussianBlur(src, (0, 0), 10)
#(0,0)을 넣으면 알아서 결정하겠다 라는 뜻이다.
#시그마 값은 1정도 주겠다. 내부적으로 7by7정도 ~9by9
dst2 = cv2.blur(src, (21,21))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
