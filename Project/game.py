import pygame
from world import World
from services import blit_rotate
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

angle = 0
done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

        elif event.type == QUIT:
            done = True


    pos = (screen.get_width() / 2, screen.get_height() / 2)

    blit_rotate(screen, world.surf, pos, (world_width / 2, world_height / 2), angle)
    angle += 1.2

    pygame.display.flip()

pygame.quit()
exit()
