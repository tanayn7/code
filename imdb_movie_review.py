# -*- coding: utf-8 -*-
"""IMDB_movie_review.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iuUJB4H3h6Rw56NkZlj8Z5iw5ljU51Ak
"""

import numpy as np

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten

from tensorflow.keras.datasets import imdb
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=200)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=200)

model = Sequential()
model.add(Embedding(10000, 128, input_length=200)) #10000 is max features
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)

model.evaluate(x_test,y_test)

pred_val = model.predict(x_test).flatten()

ans = np.where(pred_val <0.5 ,0,1 )

ans[43]

review = x_test[44]

word_to_index = imdb.get_word_index()

index_to_word = { index : word for word, index in word_to_index.items()}

words = [ index_to_word.get(i-3,'?') for i in review]
final_text = ' '.join(words)

final_text