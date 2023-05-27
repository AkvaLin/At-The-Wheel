import arcade
from world import World
from player import Player
from obstacleSpawner import ObstacleSpawner

SCREEN_TITLE = 'At The Wheel'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class AtTheWheel(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

        self.world = None
        self.scene = None
        self.player = None
        self.angle = 1080
        self.obstacle_amount = 3
        self.spawner = ObstacleSpawner()
        self.is_collision = False
        self.current_collision = None

    def setup(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.world = World()
        self.scene = arcade.Scene()
        self.scene.add_sprite('World', self.world)
        self.world.set_boundaries()
        for bound in self.world.boundaries_list:
            self.scene.add_sprite('Boundary', bound)
        self.spawner.setup()
        for _ in range(self.obstacle_amount):
            self.spawner.spawn(self.scene)
        self.player = Player(max_hp=3)
        self.scene.add_sprite('Player', self.player)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.world.on_update(self.angle, delta_time)
        self.angle = 1080
        for boundary in self.world.boundaries_list:
            if arcade.check_for_collision(self.player, boundary):
                self.angle = 500
        for obstacle in self.spawner.obstacles_list:
            if arcade.check_for_collision(self.player, obstacle) and not self.is_collision:
                self.player.get_damage()
                self.is_collision = True
                self.current_collision = obstacle
            elif obstacle == self.current_collision and self.is_collision:
                if not arcade.check_for_collision(self.player, self.current_collision):
                    self.current_collision = None
                    self.is_collision = False
            obstacle.rotate_around_point(self.world.position, self.angle * delta_time)
        self.player.on_update(delta_time)
