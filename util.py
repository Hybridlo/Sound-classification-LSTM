import numpy as np

def get_class_categorical(filename):
    first_dash_index = filename.index('-')
    c = int(filename[first_dash_index+1])
    result = np.zeros(10)
    result[c-1] = 1
    result = result.reshape(1, 10)
    return result

a = get_class_categorical('7061-6-0-0')
if True:
    pass