import pygame
class Character:
    def __init__(self,x,y,speed,image,scale):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
    def move(self,keys):
        if keys[pygame.K_LEFT] :
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] :
            self.rect.x += self.speed
        if keys[pygame.K_UP] :
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] :
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)