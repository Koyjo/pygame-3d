import numpy as np
from Render3D.Shape.Shape import Shape


class Plane(Shape):

    def __init__(self, start, vec1, vec2, size1, size2, number1, number2):
        super().__init__()

        nodes = [[start[k] + vec1[k] * size1 * i + vec2[k] * size2 * j for k in range(0, 3)] for i in
                 range(0, number1 + 1) for j in range(0, number2 + 1)]
        cube_nodes = np.array(nodes)
        print(len(nodes))
        self.addNodes(cube_nodes)
        faces = [[i+(number2+1)*j, i+1+(number2+1)*j, i+1+(number2+1)*(j+1), i+(number2+1)*(j+1)] for i in range(0, number1) for j in range(0, number2)]
        self.addFaces(faces)
