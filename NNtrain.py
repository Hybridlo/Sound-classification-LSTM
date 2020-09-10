import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.compat.v1 import ConfigProto, InteractiveSession

from traverse import sounds, count_amount_of_files

config = ConfigProto()
config.gpu_options.allow_growth = True      #crash without it
session = InteractiveSession(config=config)

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
    validation_steps=count_amount_of_files(list(range(10))),
    callbacks=[ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5')],
)

model.save_weights('model1.h5')