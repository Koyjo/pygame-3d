from Render3D.Shape.Shape import Shape


class Model(Shape):

    def __init__(self, file):
        super().__init__()
        with open(file, 'r') as f:
            pass