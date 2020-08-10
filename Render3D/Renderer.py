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
        self.movingCamera = False
        ViewPoint.move(0, -0.5, -1)

    def event(self, event):
        if event.type == pygame.KEYDOWN:

            print(ViewPoint.Camera.matrix)
            #Rotate
            if event.unicode == 'q':
                ViewPoint.rotate(0, 0.1, 0)
            elif event.unicode == 'd':
                ViewPoint.rotate(0, -0.1, 0)
            #Translate
            elif event.unicode == 'z':
                ViewPoint.move(0, 0, 0.1)
            elif event.unicode == 's':
                ViewPoint.move(0, 0, -0.1)
            elif event.unicode == 'a':
                ViewPoint.move(0.1, 0, 0)
            elif event.unicode == 'e':
                ViewPoint.move(-0.1, 0, 0)
            elif event.unicode == 'y':
                ViewPoint.rotateAbs('x', -0.1)
            elif event.unicode == 'u':
                ViewPoint.rotateAbs('x', 0.1)

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event. button == 1:

                self.movingCamera = True

        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                self.movingCamera = False

        if self.movingCamera:

            if event.type == pygame.MOUSEMOTION:
                ViewPoint.rotateAbs('x', -event.rel[1]/500)
                ViewPoint.rotateAbs('y', -event.rel[0] / 500)
        pass

    def update(self):
        print(ViewPoint.Camera.position)
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