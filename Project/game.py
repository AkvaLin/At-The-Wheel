import pygame
from steeringwheel import steering
from world import World
from services import blit_rotate
from player import Player
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

pygame.display.set_caption("At The Wheel")

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((64, 140, 135))

clock = pygame.time.Clock()

world = World()
world_width, world_height = world.surf.get_size()

player_x_default = 415
player_x_max = 510
player_x_min = 320

player_x = player_x_default
player_y = 360

player_offset = 5

player = Player(3)

angle = 0
counter = 0
turn = 0
done = False
while not done:
    clock.tick(60)
    counter += 1
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

        elif event.type == QUIT:
            done = True

    if counter == 6:
        turn = steering()
        counter = 0

    if turn == -1:
        if player_x_min <= player_x - player_offset:
            player_x -= player_offset
    elif turn == 1:
        if player_x_max >= player_x + player_offset:
            player_x += player_offset

    pos = (screen.get_width() / 2, screen.get_height() / 2)

    blit_rotate(screen, world.surf, pos, (world_width / 2, world_height / 2), angle)
    screen.blit(player.surf, (player_x, player_y))
    angle += 1.2

    pygame.display.flip()

pygame.quit()
exit()
