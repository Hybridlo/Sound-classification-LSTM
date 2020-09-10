import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"	#slows training process but crashes without it

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

from traverse import sounds, count_amount_of_files

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
    metrics=['accuracy'],
)

model.fit(
    sounds([10], 64),
    epochs=64,
    steps_per_epoch=count_amount_of_files([10]),
    validation_data=sounds(list(range(10)), 64),
    validation_steps=count_amount_of_files(list(range(10)))
)

model.save_weights('model1.h5')