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
        self.boundaries_list.append(Boundary(260, 600, -10, 0.2))
        self.boundaries_list.append(Boundary(645, 360, 50, 0.11))
        self.boundaries_list.append(Boundary(710, 430, 0, 0.08))
        self.boundaries_list.append(Boundary(730, 445, 45, 0.06))
        self.boundaries_list.append(Boundary(590, 300, 75, 0.08))
        self.boundaries_list.append(Boundary(615, 300, 75, 0.08))
        self.boundaries_list.append(Boundary(594, 253, -75, 0.08))
        self.boundaries_list.append(Boundary(615, 215, -75, 0.05))
        self.boundaries_list.append(Boundary(530, 510, -35, 0.075))
        self.boundaries_list.append(Boundary(505, 470, -80, 0.057))
        self.boundaries_list.append(Boundary(555, 545, -80, 0.057))
        self.boundaries_list.append(Boundary(780, 220, 0, 0.02))
        self.boundaries_list.append(Boundary(770, 207, 0, 0.02))
        self.boundaries_list.append(Boundary(760, 190, 0, 0.02))
        self.boundaries_list.append(Boundary(750, 177, 0, 0.02))
        self.boundaries_list.append(Boundary(740, 167, 0, 0.015))
        self.boundaries_list.append(Boundary(790, 230, 0, 0.02))
        self.boundaries_list.append(Boundary(800, 250, 0, 0.02))
        self.boundaries_list.append(Boundary(810, 270, 0, 0.018))
        self.boundaries_list.append(Boundary(820, 290, 0, 0.013))
        self.boundaries_list.append(Boundary(825, 305, 0, 0.013))
        self.boundaries_list.append(Boundary(830, 320, 0, 0.013))
        self.boundaries_list.append(Boundary(835, 335, 0, 0.007))
        self.boundaries_list.append(Boundary(840, 350, 0, 0.007))
