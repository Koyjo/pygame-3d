import numpy as np
import pygame
from Render3D.ViewPoint import Camera


def computePCamera(node, camera):
    """
    Compute a node coordinate relative to camera
    :param node: np.array[4] node coordiantes
    :param camera: np.array[4,4] camera transform matrix
    :return: node coordinates relative to camera
    """
    return node.dot(camera)


def computePixelCoordinate(pCamera):
    """
    Compute the pixel coordinates of a given point
    :param pCamera: np.array[3] coordinates of the point relative to the camera
    :return: pRaster : np.array[2] pixel coordinates of the point
             visible : bool indicating if the point is visible from the camera
    """
    t = -0.1
    r = 0.1

    pScreen = [pCamera[0] / - pCamera[2] * 0.1, pCamera[1] / - pCamera[2] * 0.1]
    pNDC = [(pScreen[0] + r) / (2 * r), (pScreen[1] + t) / (2 * t)]
    pRaster = [int(pNDC[0] * 800), int((pNDC[1]) * 800)]
    visible = False
    if 0 < pRaster[0] < 800 and 0 < pRaster[1] < 800:
        visible = True
    return pRaster, visible


class Shape:

    def __init__(self, color=pygame.color.Color(255, 255, 255), edge_color=pygame.color.Color(0, 0, 0)):
        self.nodes = np.zeros((0, 4))
        self.faces = []
        self.nodes_pcamera = []
        self.color = color
        self.edge_color = edge_color

    def render(self, window):
        self.nodes_pcamera = [computePCamera(node, Camera.matrix) for node in self.nodes]
        for face in self.sortedFaces():
            self.projection(face, window)

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    def addFaces(self, triangles_list):
        self.faces += triangles_list

    def sortedFaces(self):
        """
        Sort the faces list of the shape by distance to the camera
        :return: sorted faces
        """
        sorted_faces = sorted(self.faces, key=lambda face: min(self.nodes_pcamera[i][2] for i in face))
        return sorted_faces

    def setColor(self, color):
        self.color = color

    def projection(self, face, window):
        """
        Compute the pixel coordinates of all nodes in a given face and draw the face and edges if visible
        note : the node coordinate relative to camera must be computed beforehand an stored in nodes_pcamera
        :param face: face to draw
        :param window: pygame window to display in
        """
        pointlist = []
        visible = False
        for i in face:
            if self.nodes_pcamera[i][2] < 0:
                coord, nodeVisible = computePixelCoordinate(self.nodes_pcamera[i])
                if nodeVisible:
                    visible = True
                pointlist.append(coord)
            elif self.nodes_pcamera[i][2] == 0:
                return

        if visible:
            pygame.draw.polygon(window, self.color, pointlist)

            for i in range(0, len(pointlist)):
                start = pointlist[i % len(face)]
                end = pointlist[(i + 1) % len(face)]
                pygame.draw.aaline(window, self.edge_color, start, end)

    def transform(self, matrix):
        self.nodes = np.dot(self.nodes, matrix)
