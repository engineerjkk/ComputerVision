import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)
#커널은 가급적으로 0,0 / 시그마는 2정도로 주자.
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)
#입력영상은 두배로하고 blr빼기

#dst=cv2.addWeighted(src,1,blr,-1,128)
#addWeighted로 subtract를 구현해보기
#첫번째 영상은 1의 가중치를, 두번째는 -1의 가중치를 그 결과에 128을 더한다.
#dst=cv2.subtract(src,blr)
#dst=src-blr
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
