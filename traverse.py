# sounds folder is git ignored
import os
from audio import get_mel_spec
from util import get_class_categorical
import time

default_path = 'sounds\\audio'

def sound_files(skip=[-1]):
    for rel_path, dirs, files in os.walk(default_path):

        if rel_path == default_path:
            continue

        fold = rel_path[-2:]
        if not fold[0].isdigit():
            fold = fold[1]
        fold_num = int(fold)

        if fold_num not in skip:
            for f in files:
                yield (rel_path, f)

def sounds(skip=[-1], epochs=64):
    for i in range(epochs):
        sf = sound_files(skip)
        for f in sf:
            start = time.perf_counter()
            r = get_mel_spec(f[0] + '\\' + f[1])
            print('Time:', (time.perf_counter() - start)*1000, "ms")
            yield (r, get_class_categorical(f[1]))

def count_amount_of_files(skip=[-1]):
    i = 0

    for rel_path, dirs, files in os.walk(default_path):

        if rel_path == default_path:
            continue

        fold = rel_path[-2:]
        if not fold[0].isdigit():
            fold = fold[1]
        fold_num = int(fold)

        if fold_num not in skip:
            for f in files:
                i += 1

    return i