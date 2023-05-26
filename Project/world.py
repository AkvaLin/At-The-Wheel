import pygame


class World(pygame.sprite.Sprite):
    def __init__(self):
        super(World, self).__init__()
        image = pygame.image.load('sprites/Track.png').convert()
        image = pygame.transform.scale(image, (720, 720))
        self.surf = image
        self.rect = self.surf.get_rect()
