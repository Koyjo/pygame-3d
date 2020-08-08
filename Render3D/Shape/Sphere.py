import numpy as np
from Render3D.Shape.Shape import Shape


class Sphere(Shape):

    def __init__(self, x, y, z, radius, resolution):
        super().__init__()
        latitudes = [n * np.pi / resolution for n in range(1, resolution)]
        longitudes = [n * 2 * np.pi / resolution for n in range(resolution)]

        # Add nodes except for poles
        self.addNodes(
            [(x + radius * np.sin(n) * np.sin(m), y - radius * np.cos(m), z - radius * np.cos(n) * np.sin(m)) for m in latitudes for
             n in longitudes])

        # Add square faces to whole spheroid but poles
        num_nodes = resolution * (resolution - 1)
        self.addFaces([(m + n, (m + resolution) % num_nodes + n,
                            (m + resolution) % resolution ** 2 + (n + 1) % resolution, m + (n + 1) % resolution) for n
                           in range(resolution) for m in range(0, num_nodes - resolution, resolution)])

        # Add poles and triangular faces around poles
        self.addNodes([(x, y + radius, z), (x, y - radius, z)])
        self.addFaces([(n, (n + 1) % resolution, num_nodes + 1) for n in range(resolution)])
        start_node = num_nodes - resolution
        self.addFaces([(num_nodes, start_node + (n + 1) % resolution, start_node + n) for n in range(resolution)])
