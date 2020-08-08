import numpy as np
import pygame
from Render3D import ViewPoint


class Renderer:

    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.window = window
        self.shapes = {}
        self.background = pygame.color.Color(174, 225, 238)
        self.basicFont = pygame.font.SysFont("Arial", 22)
        ViewPoint.move(0, 1, 0)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'a':
                ViewPoint.rotate(0, 0.1, 0)
            elif event.unicode == 'e':
                ViewPoint.rotate(0, -0.1, 0)
            elif event.unicode == 'z':
                ViewPoint.move(0, 0, 0.1)
            elif event.unicode == 's':
                ViewPoint.move(0, 0, -0.1)
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
        """
        Compute and displays the current frame rate
        """
        fps = str(int(self.clock.get_fps()))
        fps_text = self.basicFont.render(fps, 1, pygame.Color("coral"))
        self.window.blit(fps_text, (20,20))