import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image
#가로가 320이고 세로가 240으로 되어있는 이미지를 그레이스케일로, 엠프티를썼기에 픽셀은 쓰레기값으로 채워진다.
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image
#컬러영상이다. 제로스를 썼기때문에 컬러여도 모든픽셀이 0이기에 검정색으로된다. 
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray
#원스함수를 이용하게 되면 모든 픽셀이 1로된다. 0과 1은 눈으로는 구분을 못하기에 그냥 검정색이다.그런데 여기다가 255를 곱해서 이미지를 하얀색으로 출력해줄 수 있다.
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow
#풀이라는 함수를 이용해서 만들고, 풀함수는 인자구성이 fillVaule가 중간에 들어가므로
#여기서는(0,255,255) 노랑색으로 설정을 해 주었다.
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1
img3 = img1.copy()
#adarray에서 지원하는 카피 함수
#여기서 img2가 img1에 있는 데이터를 같이 쓴다. 
#하지만 카피를 하면 메모리를 새로할당하기 때문에 다르다. 
#img1.fill(255)
#img1[:,:]=(0,255,255) #img1에 따라 img2도 영향을 받게된다. 

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
#인덱싱, 슬라이싱 방법을 쓰면 된다.
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
#40번째 행부터 120번째 항까지, 30번째 열부터 150번째 열까지 img2에 할당한다.
img3 = img1[40:120, 30:150].copy()
#마찬가지로 이것만 긁어서 카피해서 img3에다가 넣을 수 있다.
#하지만 
# img1[:,:]=(0,255,255)를 하게되면 img2 역시 영향을 받게된다.
#img2.fill(0)
#그런데 만약 img2를 0으로 다 채워도 img1에 영향을 받게된다.
#이런것 처럼 img2를 특정 ROI식으로 사용해 img1을 처리해 줄 수 있다.
cv2.circle(img2,(50,50),20,(0,0,255),2) 
#img2 를 그리는데 좌표 50 50, 반지름 20, 레드, 두께는 2하면 
#난 코드를 img2에다가 했는데 img1에 영향을 줄 수 있다.

#즉 슬라이싱 방법을 이용해서 ROI를 쓸수있다. 관심영역인 것이다.
#region of interest
#마스크 연산에서 다룰 수 있다.

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
