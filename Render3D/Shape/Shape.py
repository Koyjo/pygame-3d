import numpy as np
import pygame
from Render3D.ViewPoint import ViewPoint


class Shape:

    def __init__(self, color=pygame.color.Color(255, 255, 255), edge_color=pygame.color.Color(0, 0, 0)):
        self.nodes = np.zeros((0, 4))
        self.faces = []
        self.nodes_pcamera = []
        self.color = color
        self.edge_color = edge_color

    def render(self, window):
        self.nodes_pcamera = [self.computePCamera(node) for node in self.nodes]
        for face in self.sortedFaces():
            self.projection(face, window)

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    def addFaces(self, triangles_list):
        self.faces += triangles_list

    def sortedFaces(self):
        sorted_faces = sorted(self.faces, key=lambda face: min(self.nodes_pcamera[i][2] for i in face))
        return sorted_faces

    def setColor(self, color):
        self.color = color

    def getBoundingBox(self):
        return [np.min(self.nodes, axis=0), np.max(self.nodes, axis=0)]

    def projection(self, face, window):
        pointlist = []
        visible = False
        for i in face:
            coord, nodeVisible = self.computePixelCoordinate(self.nodes_pcamera[i])
            if nodeVisible:
                visible = True
            pointlist.append(coord)

        if visible:
            pygame.draw.polygon(window, self.color, pointlist)

            for i in range(0, len(pointlist)):
                start = pointlist[i % len(face)]
                end = pointlist[(i + 1) % len(face)]
                pygame.draw.aaline(window, self.edge_color, start, end)

    def computePCamera(self, node):
        worldToCamera = np.linalg.inv(ViewPoint.camera)
        return np.dot(node, worldToCamera)

    def computePixelCoordinate(self, pCamera):
        t = -0.1
        r = 0.1

        pScreen = [pCamera[0] / - pCamera[2] * 0.1, pCamera[1] / - pCamera[2] * 0.1]
        pNDC = [(pScreen[0] + r) / (2 * r), (pScreen[1] + t) / (2 * t)]

        pRaster = [int(pNDC[0] * 800), int((1 - pNDC[1]) * 800)]
        visible = False
        if 0 < pRaster[0] < 800 and 0 < pRaster[1] < 800 and pCamera[2] < 0:
            visible = True
        return pRaster, visible

    def transform(self, matrix):
        self.nodes = np.dot(self.nodes, matrix)
