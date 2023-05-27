from boundary import Boundary
import arcade
import math


class World(arcade.Sprite):
    def __init__(self):
        super().__init__('sprites/Track.png', center_x=640, center_y=360, scale=0.5)
        self.boundaries_list = arcade.SpriteList()

    def on_update(self, angle, delta_time: float = 1 / 60):
        self.angle += math.radians(angle) * delta_time
        for boundary in self.boundaries_list:
            boundary.rotate_around_point(self.position, angle * delta_time)

    def set_boundaries(self):
        self.boundaries_list.append(Boundary(326, 380, 17, 0.1))
        self.boundaries_list.append(Boundary(312, 430, 17, 0.1))
        self.boundaries_list.append(Boundary(337, 300, -5, 0.1))
        self.boundaries_list.append(Boundary(337, 200, 12, 0.1))
        self.boundaries_list.append(Boundary(387, 103, 45, 0.1))
        self.boundaries_list.append(Boundary(500, -5, -2, 0.2))
        self.boundaries_list.append(Boundary(650, 40, 50, 0.08))
        self.boundaries_list.append(Boundary(680, 10, -3, 0.08))
        self.boundaries_list.append(Boundary(850, -8, -55, 0.2))
        self.boundaries_list.append(Boundary(970, 120, -34, 0.2))
        self.boundaries_list.append(Boundary(1004, 300, -15, 0.1))
        self.boundaries_list.append(Boundary(1015, 400, 0, 0.1))
        self.boundaries_list.append(Boundary(998, 500, 15, 0.1))
        self.boundaries_list.append(Boundary(948, 585, 50, 0.1))
        self.boundaries_list.append(Boundary(850, 656, 55, 0.1))
        self.boundaries_list.append(Boundary(750, 710, 70, 0.1))
        self.boundaries_list.append(Boundary(650, 738, 80, 0.1))
        self.boundaries_list.append(Boundary(630, 735, -80, 0.1))
        self.boundaries_list.append(Boundary(530, 728, 90, 0.1))
        self.boundaries_list.append(Boundary(310, 670, 45, 0.2))
        self.boundaries_list.append(Boundary(260, 600, -10, 0.2))
