import sys
import numpy as np
import cv2


# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS) #24 프레임
effect_frames = int(fps * 2) #48프레임

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):#뒤에 48프레임정도 남겨두고 output에다가 저장
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error!')
        sys.exit()

    out.write(frame1)
    print('.', end='')

    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames): #effect_frames 에서 합성하는 구간이다.
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    dx = int(w / effect_frames) * i
    #w를 effect_frames로 나눈다. 1280/48=27
    #가로 27픽셀 단위로 짤리게 된다.
    #27프레임 54프레임~~ 단위로 증가한다.
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    #세로크기, 가로크기, 컬러영상이니까 3
    #frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    #frame[:, dx:w, :] = frame1[:, dx:w, :]
    #프레임 영상의 구성

    alpha = i / effect_frames
    frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)
    #1-alpha와 alpha의 합이 1이 되어야 한다. (가중치)

    out.write(frame)
    print('.', end='')

    cv2.imshow('output', frame)
    cv2.waitKey(delay)

# 2번 동영상을 복사, effect 끝나고 2번째 동영상 이어붙이디.
for i in range(effect_frames, frame_cnt2):#effectframe 부터 끝까지
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error!')
        sys.exit()

    out.write(frame2)
    print('.', end='')

    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

print('\noutput.avi file is successfully generated!')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
