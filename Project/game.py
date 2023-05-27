from player import Player
import arcade
from world import World
from obstale import Obstacle

SCREEN_TITLE = 'At The Wheel'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class AtTheWheel(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

        self.world = None
        self.scene = None
        self.player = None
        self.obstacle = None
        self.angle = 1080

    def setup(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.world = World()
        self.scene = arcade.Scene()
        self.scene.add_sprite('World', self.world)
        self.world.set_boundaries()
        for bound in self.world.boundaries_list:
            self.scene.add_sprite('Boundary', bound)
        self.player = Player(max_hp=3)
        self.scene.add_sprite('Player', self.player)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.world.on_update(self.angle, delta_time)
        self.angle = 1080
        for asd in self.world.boundaries_list:
            if arcade.check_for_collision(self.player, asd):
                self.angle = 500
        # self.obstacle.rotate_around_point(self.world.position, self.angle * delta_time)
        self.player.on_update(delta_time)