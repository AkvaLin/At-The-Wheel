import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        image = pygame.image.load('sprites/Obstacle.png').convert()
        image = pygame.transform.scale(image, (30, 30))
        self.surf = image
        self.rect = self.surf.get_rect()
