import sys
import numpy as np
import cv2


# CrCb 살색 히스토그램 구하기
ref = cv2.imread('kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)
#살색 히스토그램에 부함하는 픽셀을 미리 마스크로 만든다.
if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
#마스크부분이있는데 입력영상 전체하고싶으면 None을 주고, 특정영역에서만 히스토그램 주고싶으면 마스크를 사용한다.
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)
#히스트가 가질수있는범위를 0~255로하고, 결과영상의 데이터를 그레이로 했다.
#히스토그램이 너무크면 큰것만 밝게나오고 작은건 다 0에가깝게 나오기때문에 log를 취하는게 좋다. 근데 혹시 이게 0일수도있으니 그 부분을 대비하여 1을 더해준다.

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)


cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
