import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

from traverse import sounds

model = Sequential([
    LSTM(128, input_shape=(None, 128), return_sequences=True),
    Dropout(0.25),
    LSTM(64),
    Dropout(0.25),
    Dense(10, activation='softmax'),
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['Accuracy'],
)

model.fit(
    sounds([10]),
    epochs=64
)

model.save_weights('model1.h5')