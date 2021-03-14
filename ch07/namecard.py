"""
Tesseract-ocr 설치하기

1. tesseract-ocr-w64-setup-v5.0.0-alpha.20200328 파일 다운로드 
   (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe)
2. 설치 시 "Additional script data" 항목에서 "Hangul Script", "Hangul vertical script" 항목 체크,
   "Additional language data" 항목에서 "Korean" 항목 체크.
4. 설치 후 시스템 환경변수 PATH에 Tesseract 설치 폴더 추가
   (e.g.) c:\Program Files\Tesseract-OCR
4. 설치 후 시스템 환경변수에 TESSDATA_PREFIX를 추가하고, 변수 값을 <Tesseract-DIR>\tessdata 로 설정
5. <Tesseract-DIR>\tessdata\script\ 폴더에 있는 Hangul.traineddata, Hangul_vert.traineddata 파일을
   <Tesseract-DIR>\tessdata\ 폴더로 복사
6. 명령 프롬프트 창에서 pip install pytesseract 명령 입력
"""

import sys
import random
import numpy as np
import cv2
import pytesseract


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    #lexsort를 이용해서 컬럼 0-> 1번 순서로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts
#좌측상단부터 반시계로 저장되는 pts를 리턴

# 영상 불러오기
filename = 'namecard1.jpg'
if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()

# 출력 영상 설정
dw, dh = 720, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
#좌측상단부터 반시계방향으로 돌면서 저장.
dst = np.zeros((dh, dw), np.uint8)
#출력으로 만들 dst영상 만들기

# 입력 영상 전처리
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#그레이스케일 변환
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#오츠로 자동 이진화
# 외곽선 검출 및 명함 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#findContours로 외곽선 검출 모드는 EXTERNAL로 해서 바깐쪽만 설정 홀은 필요없으니까

cpy = src.copy()
for pts in contours:
    # 너무 작은 객체는 무시
    if cv2.contourArea(pts) < 1000: #노이즈 제거
        continue

    # 외곽선 근사화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    #어느정도 큰 객체는 다 근사과

    # 컨벡스가 아니고, 사각형이 아니면 무시
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue
        #컨백스인지 사각형아닌지 검사

    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    #polylines로 외곽선 그리기
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    #reorderPts 명함에서 좌측상단 0, 좌측하단 1, 우측하단 2, 우측상단 3으로 만듦
    #approx로 ndarray에 들어가있는 점들을 분석해서 좌측상단부터 반시계방향으로 리오더해서 src에 저장해준다.
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
#perspectiveTransform하고
dst = cv2.warpPerspective(src, pers, (dw, dh))
#warpPerspective 이용해서 똑바로 펴는 작업을 한다.
dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
#그레이 스케일로 이미지 변환
print(pytesseract.image_to_string(dst_gray, lang='Hangul+eng'))
#numpy, ndarray 지원. 컬러영상일 경우, 내부적으로 rgb이므로 cvt를 해줘야한다. 근데 그냥 대부분 그레이스케일로 한다.
#language를 한글과 영어 둘다 사용해라라는 옵션을 준다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
