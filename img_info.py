import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
#cat.bmp 파일을 그레이스케일로 불러와서 img1에다가 넣는다.
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()
print(type(img1))
print(img1.shape)#2차원
print(img2.shape)#3차원으로 출력된다.
print(img1.dtype)
print(img2.dtype)#똑같이 uint8로 출력된다.
# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)

# 영상의 크기 참조
h, w = img2.shape[:2]
print('img2 size: {} x {}'.format(w, h))
#가로가 640, 세로가 480 이 뜬다.

if len(img1.shape) == 2: #img1.ndim ==2 해도 똑같다.
    #shape이라는 튜플값이 2이냐,
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0, 0, 255)        

# img1[:,:] = 255
# img2[:,:] = (0, 0, 255) 

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()

#h,w=img2.shape[:2] #shape 튜플의 앞게꺼 두개만 받겠다. 그러면 컬러영상이어도 가로세로만
#나오니 에러가 뜨니 않는다. 컬러영상의 경우 세개라서 h,w로만 받으면 두개니 에러가 뜨는데 말이다.

#이미지의 픽셀값을 알고싶으면
#x=2
#y=10 한 다음에
#p1=img1[y,x] 해주면 된다. 행 열순이기에 y,x이다. 
#print(p1)

#여기서 BGR순서 알기

#그렇기 때문에 img[y,x]=0하면 이 위치에 0값의 픽셀(검정)을 대입할 수 있다.
#img2[y,x]=(0,0,255)로 하게되면 빨간색을 넣는다.

#하지만 for루프를 돌면서 영상의 픽셀작업은 하면 안된다.
#엄청나게 느리다. 한두장이야 실행해도 곧바로 나타나는 것처럼 보이지만 딜레이가있다.
#이걸 동영상에서 하면 엄청나게 느리다는 것을 볼 수 있다.

#가급적이면 오픈시비나 넘파이에서 제공하는 방법을 사용하자.

# img1[:,:] = 255
# img2[:,:] = (0, 0, 255) for 루프대신에 이걸써야됨. 이런식의 범위를 지정한다. 
#결과는 동일하지만 이게 훨씬 빠르다. 