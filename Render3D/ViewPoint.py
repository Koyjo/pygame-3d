import numpy as np


class ViewPoint:

    position = np.array([0, 0, 0])
    camera = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, -1, -1],
                       [0, 0, 0, 1]])

    '''np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, -1, -1],
         [0, 0, -1, 0]])
    '''