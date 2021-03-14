import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
#src의 height와 width를 받는다. 
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))
#결과영상의 크기를 인자로 잘 줘야한다. 0,0으로하면 입력영상과 동일하므로 바꿔줘야한다.
#세로크기는 같다.하지만 W가 h*0.5만큼 저 길어야한다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
