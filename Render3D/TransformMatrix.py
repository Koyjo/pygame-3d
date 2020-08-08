import numpy as np

"""
Transform Matrix for all Basic Transformations
"""


def rotate(p, x=0, y=0, z=0):
    """
    Matrix for a rotation along the object's own axis
    :param p: position of the object
    :param x: rotation around its x axis (in radians)
    :param y: rotation around its y axis (in radians)
    :param z: rotation around its z axis (in radians)
    :return: resulting transform matrix
    """
    return translate(-p[0], -p[1], -p[2]).dot(rotateX(x)).dot(rotateY(y)).dot(rotateZ(z)).dot(
        translate(p[0], p[1], p[2]))


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
