import sys
import numpy as np
import cv2


src = cv2.imread('cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
#_,dst1 으로 인자 두개로 받아야 한다.
#100으로 스레시홀드 지정
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)
#210 스레시홀드로 2진화
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)#염색세포 검출
cv2.imshow('dst2', dst2)#모든세포 검출
cv2.waitKey()
cv2.destroyAllWindows()
