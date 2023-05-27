import arcade
import math


class Boundary(arcade.Sprite):
    def __init__(self, x, y, angle, scale):
        super().__init__('sprites/boundary.jpg', center_x=x, center_y=y, angle=angle, scale=scale)
        self.alpha = 0

    def rotate_around_point(self, point, degrees, change_angle=True):
        if change_angle:
            self.angle += math.radians(degrees)

        self.position = arcade.rotate_point(
            self.center_x, self.center_y,
            point[0], point[1], math.radians(degrees))