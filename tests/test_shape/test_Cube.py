from unittest import TestCase

from Render3D.Shape import Cube


class TestCuboid(TestCase):

    def setUp(self):
        self.cube = Cube.Cuboid(0, 0, 0, 100, 100, 100)

    def test_Nodes(self):
        self.assertTrue(True)