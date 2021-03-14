import sys
import cv2

#src에서 비행기만 짤라서 dst 부분에 넣기
# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
#마스크는 포토샵같은 이미지 편집 툴을 통해서 만들면 된다.
#물론 이것도 알고리즘으로 만들수는 있다.
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src, mask, dst)
#src에서 마스크를 이용해서 dst를 만들고 싶다.
#이 모두 세개는 사이즈가 같아야하고
#src와 dst는 타입이같아야한다. 그레이면 그레이, 컬러면 컬러 마스크는 무조건 그레이타입
# dst[mask > 0] = src[mask > 0]
#0보다 크다는것은 트루를 리턴한다. 메모리를 새롭게 복사가아닌 
#참조형태로 복사를 한다.
#dst 영상의 픽셀값 자체가 바뀐다.
#dst=cv2.copyTo(src,mask)를 하면 비어있는 검정색에 비행기만 들어간다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
#포토샵 이미지를 그대로 가져오려면 IMREAD_UNCHANGED 로 해야함을 유의!
#디버깅해서 보면 logo는 채널수가 4임! shape(222,180,4)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

src=cv2.imread('opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
mask=src[:,:,-1] #마스크는 -1까지만 쓰겠다.
src=src[:,:,0:3] #채널이 4까지 있으니까 0~3까지 쓰겠다.
dst=cv2.imread('field.bmp',cv2.IMREAD_COROT)

h,w=src.shape[:2]
crop=dst[0:h,0:w]
#crop=dst[10:h+10,10:w+10] 위치 조정 +10씩


#cv2.copyTo(src,mask,dst)
cv2.copyTo(src,mask,crop)
#내가 이미지 크기를 바꾼것은 크롭이긴 하지만 dst자리에 crop으로 바꾸어줌으로써
#dst 이미지크기가 조정이 된다.
