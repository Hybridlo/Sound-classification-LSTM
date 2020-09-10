import numpy as np

def get_class_categorical(filename):
    first_dash_index = filename.index('-')
    c = int(filename[first_dash_index+1])
    result = np.zeros((1, 10))
    result[0][c] = 1
    return result