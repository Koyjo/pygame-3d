import pygame
import pygame.event
from pygame.locals import *

from Render3D.Renderer import Renderer
from Render3D.Shape.Sphere import Sphere


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 800))
    renderer = Renderer(window)

    #cube = Cuboid(-100, -100, 200, 100, 100, 400)
    #renderer.addShape('cube', cube)

    sphere = Sphere(0, 0, 1, 0.5, 20)
    renderer.addShape('sphere1', sphere)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            renderer.event(event)
        renderer.update()
        renderer.render()
        pygame.display.flip()


if __name__ == '__main__':
    main()
