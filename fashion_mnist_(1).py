# -*- coding: utf-8 -*-
"""fashion_mnist (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O_24XrcDafsGjCpJYZq_sanFzMMwwS-l
"""

import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense

from keras.datasets import fashion_mnist
(xtrain, ytrain) ,(xtest, ytest) = fashion_mnist.load_data()

print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)

xtrain = xtrain.reshape(-1, 28, 28, 1).astype('float32')/255.0
xtest = xtest.reshape(-1,28,28,1).astype('float32')/255.0

ytrain = keras.utils.to_categorical(ytrain)
ytest = keras.utils.to_categorical(ytest)

print(ytrain.shape)
print(ytest.shape)

model = Sequential()
model.add(Conv2D(32, activation='relu' , kernel_size=(3,3) , input_shape=(28,28,1)))
model.add(MaxPool2D( pool_size=(2,2)))
model.add(Conv2D(64, activation='relu', kernel_size=(3,3)))
model.add(MaxPool2D( pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss=keras.losses.categorical_crossentropy , optimizer= 'adam', metrics=['accuracy'])

model.fit(xtrain, ytrain , epochs=5)

model.evaluate(xtest, ytest)

pred_val = model.predict(xtest)

pred_cat = np.argmax(pred_val , axis =1)

pred_cat[0:100]

actual_cat = np.argmax(ytest, axis=1)

actual_cat[0:100]

import matplotlib.pyplot as plt

fig, axis = plt.subplots(3,3,figsize=(8,8))

for i in range(3):
    for j in range(3):
        axis[i][j].imshow(xtrain[0], cmap="gray")
