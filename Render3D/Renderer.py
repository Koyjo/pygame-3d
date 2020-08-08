import numpy as np
import pygame
from Render3D import TransformMatrix
from Render3D.ViewPoint import ViewPoint


class Renderer:

    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.window = window
        self.shapes = {}
        self.background = pygame.color.Color(174, 225, 238)
        self.basicFont = pygame.font.SysFont("Arial", 22)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'a':
                ViewPoint.camera = np.dot(ViewPoint.camera, TransformMatrix.rotateY(0.1))
            elif event.unicode == 'e':
                ViewPoint.camera = np.dot(ViewPoint.camera, TransformMatrix.rotateY(-0.1))
            elif event.unicode == 'z':
                ViewPoint.camera = np.dot(ViewPoint.camera, TransformMatrix.translate(0, 0, 0.1))
            elif event.unicode == 's':
                ViewPoint.camera = np.dot(ViewPoint.camera, TransformMatrix.translate(0, 0, -0.1))
        pass

    def update(self):
        self.clock.tick()
        pass

    def render(self):
        self.window.fill(self.background)
        [self.shapes[shape].render(self.window) for shape in self.shapes]
        self.renderFpsRate()

    def addShape(self, name, shape):
        self.shapes[name] = shape

    def renderFpsRate(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.basicFont.render(fps, 1, pygame.Color("coral"))
        self.window.blit(fps_text, (20,20))