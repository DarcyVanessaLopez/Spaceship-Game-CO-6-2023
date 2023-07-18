import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1
from game.utils.constants import ENEMY_2


class Ship_2(Enemy):
    WIDTH = 40
    HEIGTH = 60
        
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)