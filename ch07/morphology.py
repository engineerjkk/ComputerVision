import sys
import numpy as np
import cv2


src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
#가로가 5, 세로가 3 pixel로 되어있는 3행 5열의 행렬을 structure로 썼다.
dst1 = cv2.erode(src, se)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 7))
dst2 = cv2.dilate(src, se)
#그냥 단순히 3by3 팽창연산

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
