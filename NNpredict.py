from tensorflow.keras.models import load_model
from tensorflow.compat.v1 import ConfigProto, InteractiveSession
from audio import get_mel_spec
import numpy as np

config = ConfigProto()
config.gpu_options.allow_growth = True      #crash without it
session = InteractiveSession(config=config)

model = load_model('model1.h5')

def predict(filename):
    res = model.predict(get_mel_spec(filename))
    print(res)
    res = np.argmax(res)
    return res