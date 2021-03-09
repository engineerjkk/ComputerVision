# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_nonUCcU6r7qiIafOpz8XTnHg6WBH79v
"""

from keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

"""트레이닝을 먼저 시킨다. cifar10은 되게 유명한 모델이다. 이 데이터 셋 알고리즘이 다 오픈되어있다.

기본적으로레이닝을 먼저 시킨다. cifar10은 되게 유명한 모델이다. 이 데이터 셋 알고리즘이 다 오픈되어있다.

기본적으로 cifar10에 있는 자료를 keras.datasets에서 가져오게한다. 트레인과 테스트로 나눈다. 이걸 그대로 옮겨가져온다.

"""

import matplotlib.pyplot as plt
from PIL import Image

plt.figure(figsize=(10, 10))
labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

"""10개의 레이블을 제공해 이미지를 분류하려 한다.


"""

plt.figure(figsize=(10, 10))
labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
for i in range(0, 40):
    im = Image.fromarray(X_train[i])
    plt.subplot(5, 8, i + 1)
    plt.title(labels[y_train[i][0]])
    plt.tick_params(labelbottom="off",bottom="off") # x축 제거
    plt.tick_params(labelleft="off",left="off") # y축 제거
    plt.imshow(im)
plt.show()
X_train

"""여기까지가 기본적으로 트레이닝 된 것을 보여준다. 이정도면 인터넷의 있는 데이터를 잘 긁어왔음을 알 수 있다.

이제 다른것을 트레이닝 시켜보자. 
"""

import matplotlib.pyplot as plt
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout

"""위의 사이퍼를 그대로 긁어와 쓰겠다.
즉 나는 이미지를 올리지도 않았는데, 케라스에서 자동으로 데이터셋의 cifar10을 찾아서 가져온다.
"""

num_classes = 10
im_rows = 32
im_cols = 32
im_size = im_rows * im_cols * 3

"""Rows와 Cols를 지정한다."""

# 데이터 읽어 들이기 --- (*1)
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# 데이터를 1차원 배열로 변환하기 --- (*2)
X_train = X_train.reshape(-1, im_size).astype('float32') / 255
X_test = X_test.reshape(-1, im_size).astype('float32') / 255
# 레이블 데이터를 One-hot 형식으로 변환하기
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""각각을 트레인시키겠다. 지금은 시퀀셜을 스겠다."""

# 모델 정의하기 --- (*3)
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(im_size,)))
model.add(Dense(num_classes, activation='softmax'))

# 모델 컴파일하기 --- (*4)
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

"""모델컴파일하기 위해서 요소들 집어넣고,시퀀셜 카테고리 분리한다. 
categorical_crossentropy 써서 loss잡고 adam함수쓰고 실제 metrics로 정확도를 판단하겠다이다.
"""

# 학습 실행하기 --- (*5)
hist = model.fit(X_train, y_train,
    batch_size=32, epochs=50, #배치사이즈 에포크가 너무많으면 하루가넘게걸리기도한다. 50정도가 적정수치인데. 그렇다고 배치사이즈를 1로하면 의미없으니 32가 적당하다.
    verbose=1,
    validation_data=(X_test, y_test))

"""히스토그램으로 보여주는 것이다. 
한 에포크 배치가 1563개이고 그걸 다 돌린다. 

"""

# 모델 평가하기 --- (*6)
score = model.evaluate(X_test, y_test, verbose=1)
print('정답률=', score[1], 'loss=', score[0])

"""모델학습을 시켰으니 이제 평가해야한다.
평가하기가 끝나면 그래프를 그려야한다.
"""

# 학습 상태를 그래프로 그리기 --- (*7)
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""학습된 모델을 평가한뒤 그래프를 그리는 코드"""