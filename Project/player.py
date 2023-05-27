import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, max_hp):
        super(Player, self).__init__()
        image = pygame.image.load('sprites/Car.png').convert()
        image = pygame.transform.scale(image, (25, 75))
        self.surf = image
        self.rect = self.surf.get_rect()
        self.__max_hp = max_hp
        self.hp = max_hp
