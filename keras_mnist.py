# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ViJB7odh-7YRuavC5e-j9sOnGoVJ3iRw
"""

from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_imgs, train_labels),(test_imgs, test_labels) = mnist.load_data()

model=models.Sequential()
model.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
model.add(layers.Dense(10,activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

train_imgs=train_imgs.reshape((60000 , 28*28))
train_imgs=train_imgs/255

test_imgs=test_imgs.reshape((10000,(28*28)))
test_imgs=test_imgs/255

train_labels=to_categorical(train_labels)
test_labels=to_categorical(test_labels)

model.fit(train_imgs,train_labels,batch_size=32,epochs=5,verbose=2)

y=model.evaluate(test_imgs,test_labels)

type(test_imgs[0:10])

model.predict_classes(test_imgs[0:1],batch_size=1)
