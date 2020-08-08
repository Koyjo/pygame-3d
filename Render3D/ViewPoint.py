import numpy as np

from Render3D import TransformMatrix


def rotate(x, y, z):
    """
    Rotate the camera
    @:param x: Rotation along the x axis (in radians)
    @:param y: Rotation along the y axis (in radians)
    @:param z: Rotation along the z axis (in radians)
    """

    Camera.matrix = np.dot(Camera.matrix, TransformMatrix.rotate(Camera.position, x, y, z))


def move(x, y, z):
    """
    Translate the camera
    @:param x: Translation along the x axis
    @:param y: Translation along the y axis
    @:param z: Translation along the z axis
    """
    Camera.position = Camera.position + np.array([x, y, z])
    Camera.matrix = np.dot(Camera.matrix, TransformMatrix.translate(x, y, z))


class Camera:
    position = np.array([0, 0, 0])
    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, -1, -1],
                       [0, 0, 0, 1]])
