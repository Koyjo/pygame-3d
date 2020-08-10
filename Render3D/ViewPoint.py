import numpy as np

from Render3D import TransformMatrix


def rotateAbs(axis, radians):
    """
    Rotate the camera around an absolute axis
    @:param axis: axis of the rotation
    @:param radians: Rotation along the axis (in radians)
    """

    Camera.rotation[axis] += radians
    if axis == 'x':
        Camera.matrix = Camera.matrix.dot(TransformMatrix.rotateX(radians))
    elif axis == 'y':
        Camera.matrix = Camera.matrix.dot(TransformMatrix.rotateY(radians))
    elif axis == 'z':
        Camera.matrix = Camera.matrix.dot(TransformMatrix.rotateZ(radians))


def rotate(axis, radians):
    """
    Rotate the camera around an relativa axis
    @:param axis: axis of the rotation
    @:param radians: Rotation along the axis (in radians)
    """
    Camera.rotation[axis] += radians
    Camera.matrix = Camera.original_matrix \
        .dot(TransformMatrix.rotateX(Camera.rotation['x'])) \
        .dot(TransformMatrix.rotateY(Camera.rotation['y'])) \
        .dot(TransformMatrix.rotateZ(Camera.rotation['z'])) \
        .dot(TransformMatrix.translate(Camera.position['x'], Camera.position['y'], Camera.position['z']))


def move(x, y, z):
    """
    Translate the camera
    @:param x: Translation along the x axis
    @:param y: Translation along the y axis
    @:param z: Translation along the z axis
    """

    Camera.matrix = np.dot(Camera.matrix, TransformMatrix.translate(x, y, z))
    Camera.position['x'] += x
    Camera.position['y'] += y
    Camera.position['z'] += z


class Camera:
    position = {'x': 0,
                'y': 0,
                'z': 0}
    rotation = {'x': 0,
                'y': 0,
                'z': 0}
    original_matrix = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, -1, 0],
                                [0, 0, 0, 1]])
    matrix = original_matrix
