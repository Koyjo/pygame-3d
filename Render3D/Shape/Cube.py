import numpy as np
from Render3D.Shape.Shape import Shape


def generateNodes(xmin, ymin, zmin, xmax, ymax, zmax):
    return [(x, y, z) for x in [xmin, xmax] for y in [ymin, ymax] for z in [zmin, zmax]]


class Cuboid(Shape):

    def __init__(self, xmin, ymin, zmin, xmax, ymax, zmax):
        super().__init__()
        nodes = generateNodes(xmin, ymin, zmin, xmax, ymax, zmax)
        cube_nodes = np.array(nodes)
        self.addNodes(cube_nodes)
        faces = [[0, 2, 6, 4],
                 [0, 1, 5, 4],
                 [2, 3, 7, 6],
                 [4, 6, 7, 5],
                 [3, 2, 0, 1],
                 [1, 3, 7, 5]]
        self.addFaces(faces)
