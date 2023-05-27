import math
import arcade


class Obstacle(arcade.Sprite):
    def __init__(self):
        super().__init__('sprites/Obstacle.png', center_x=330, center_y=300)

    def rotate_around_point(self, point, degrees, change_angle=True):
        if change_angle:
            self.angle += math.radians(degrees)

        self.position = arcade.rotate_point(
            self.center_x, self.center_y,
            point[0], point[1], math.radians(degrees))
