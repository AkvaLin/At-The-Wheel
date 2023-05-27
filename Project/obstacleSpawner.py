import random
import arcade
from obstacle import Obstacle


class ObstacleSpawner:
    def __init__(self):
        self.spawn_points = [
            (440, 500),
            (620, 540),
            (850, 360),
            (480, 240),
            (715, 80)
        ]
        self.current_spawn_points = None
        self.obstacles_list = arcade.SpriteList()

    def setup(self):
        self.current_spawn_points = self.spawn_points

    def spawn(self, scene):
        sp = random.choice(self.current_spawn_points)
        obstacle = Obstacle(sp[0], sp[1])
        scene.add_sprite('Obstacle', obstacle)
        self.obstacles_list.append(obstacle)
        self.current_spawn_points.remove(sp)
