import numpy as np


def translate(x, y, z):
    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [x, y, z, 1]])
    return matrix


def scale(x, y, z):
    matrix = np.array([[x, 0, 0, 0],
                       [0, y, 0, 0],
                       [0, 0, z, 0],
                       [0, 0, 0, 1]])
    return matrix


def rotateX(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    matrix = np.array([[1, 0, 0, 0],
                       [0, c, -s, 0],
                       [0, s, c, 0],
                       [0, 0, 0, 1]])

    return matrix


def rotateY(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    matrix = np.array([[c, 0, s, 0],
                       [0, 1, 0, 0],
                       [-s, 0, c, 0],
                       [0, 0, 0, 1]])
    return matrix


def rotateZ(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    matrix = np.array([[c, -s, 0, 0],
                       [s, c, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matrix
