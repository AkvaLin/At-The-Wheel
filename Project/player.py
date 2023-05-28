import arcade
from steeringwheel import steering

PLAYER_X_DEFAULT = 415
PLAYER_X_MAX = 490
PLAYER_X_MIN = 220
PLAYER_Y = 360
TURN_SPEED = 100


class Player(arcade.Sprite):
    def __init__(self, max_hp):
        super().__init__('sprites/Car.png', center_x=PLAYER_X_DEFAULT, center_y=PLAYER_Y, scale=1.5)
        self.__max_hp = max_hp
        self.hp = max_hp
        self.counter = 0
        self.turn = 0

    def on_update(self, delta_time: float = 1 / 60):
        self.counter += 1

        if self.counter == 6:
            self.turn = steering()
            self.counter = 0

        if self.turn == -1 and PLAYER_X_MIN <= self.center_x - TURN_SPEED:
            self.center_x -= TURN_SPEED * delta_time
        elif self.turn == 1 and PLAYER_X_MAX >= self.center_x - TURN_SPEED:
            self.center_x += TURN_SPEED * delta_time

    def get_damage(self):
        if self.hp > 1:
            self.hp -= 1
        else:
            return -1
