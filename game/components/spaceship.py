import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT


class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def update(self, game_speed, user_input):
        if user_input[pygame.K_LEFT]:
             self.move_left(game_speed)
             
        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)
            
        if user_input[pygame.K_UP]:
            self.move_up(game_speed)
        
        if user_input[pygame.K_DOWN]:
            self.move_down(game_speed)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
#tarea clase 1
        
    def move_left(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
            
    def move_right(self, game_speed):
        self.rect.x += game_speed
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = -self.rect.width
            
    def move_up(self, game_speed):
        self.rect.y -= game_speed
        if self.rect.bottom < SCREEN_HEIGHT/ 2:
            self.rect.y = SCREEN_HEIGHT
            
    def move_down(self, game_speed):
        self.rect.y += game_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height

        
        
        
        