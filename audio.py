import numpy as np
import librosa
from functools import lru_cache

@lru_cache(None)
def get_mel_spec(filename):
    sound, sr = librosa.load(filename)
    # sound, _ = librosa.effects.trim(sound)

    n_fft = 2048
    hop_length = 512
    n_mels = 128
    S = librosa.feature.melspectrogram(sound, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    S_DB = librosa.power_to_db(S, ref=np.max)
    result = librosa.util.normalize(S_DB) + 1
    result = result.transpose()
    result = result.reshape((1,) + result.shape)
    return result