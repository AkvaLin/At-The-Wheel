import arcade
from world import World
from player import Player
from obstacleSpawner import ObstacleSpawner
from pydispatch import dispatcher

ANGLES = (720, 1080, 1440)


class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        self.world = None
        self.scene = None
        self.player = None
        self.selected_angle = None
        self.angle = None
        self.obstacle_amount = 3
        self.spawner = ObstacleSpawner()
        self.is_collision = False
        self.current_collision = None

    def setup(self):
        self.selected_angle = 1
        self.angle = ANGLES[self.selected_angle]

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

        arcade.draw_text('Speed : ' + str(self.angle // 10), 50.0, 100.0,
                         arcade.color.BLACK, 32, 180, 'left', arcade.load_font('fonts/Roboto-Light.ttf'), True)
        arcade.draw_text('HP : ' + str(self.player.hp), 50.0, 630.0,
                         arcade.color.BLACK, 32, 180, 'left', arcade.load_font('fonts/Roboto-Light.ttf'), True)

    def on_update(self, delta_time: float):
        self.world.on_update(self.angle, delta_time)
        self.angle = ANGLES[self.selected_angle]
        for boundary in self.world.boundaries_list:
            if arcade.check_for_collision(self.player, boundary):
                self.angle = 500
        for obstacle in self.spawner.obstacles_list:
            if arcade.check_for_collision(self.player, obstacle) and not self.is_collision:
                result = self.player.get_damage()
                if result == -1:
                    dispatcher.send('defeat')
                self.is_collision = True
                self.current_collision = obstacle
            elif obstacle == self.current_collision and self.is_collision:
                if not arcade.check_for_collision(self.player, self.current_collision):
                    self.current_collision = None
                    self.is_collision = False
            obstacle.rotate_around_point(self.world.position, self.angle * delta_time)
        self.player.on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.KEY_1:
            self.selected_angle = 0
        elif symbol == arcade.key.KEY_2:
            self.selected_angle = 1
        elif symbol == arcade.key.KEY_3:
            self.selected_angle = 2
        elif symbol == arcade.key.ESCAPE:
            dispatcher.send('main')
