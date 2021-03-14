import sys
import random
import numpy as np
import cv2


src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
#오츠만으로 자동 이진화
#_, ->threshold 값 리턴되는거 안받겠다!
# src_bin 실제 2진영상
contours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#리스트형태로 모든 외곽선 검출한다.
#검출된 결과를 컨투어로 받고, 어차피 리스트로 하니 hier이 있어나 없나 똑같으니 안썼다.
#contours가 리스트니 리스트의 개수가 객체의 개수가 된다.
h, w = src.shape[:2]
dst = np.zeros((h, w, 3), np.uint8)

for i in range(len(contours)):#contours의 길이만큼 for loop를 돌겠다.
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

#첫번째 방법 
# hier 를 사용했을경우 while루프를 이용해서 index값을 증가시키는 경우 
#두번째 방법
#contour의 개수만큼 for Loop를 도는방법 
#for loop가 더 쉬울 수 있다.

#내가 찾고자하는 특정한 객체가 맞는지 잘라내는 용도로 쓸수있다.
#findContours를 좀더 공부해보자.
