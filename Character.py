import pygame
class Character:
    def __init__(self,x,y,speed,max_health,image,scale):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.max_health = max_health
        self.health = max_health
        self.immunity = False
        self.immunity_event = pygame.USEREVENT + 1
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x - self.speed > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x + self.speed < 1040 - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y + self.speed < 620 - self.rect.height:
            self.rect.y += self.speed
    def take_damage(self,damage):
        if not self.immunity:
            self.immunity = True
            print('immune')
            self.health -= damage
            print(self.health)
            pygame.time.set_timer(self.immunity_event,1000)
            if self.health <= 0:
                self.health = 0
                print("dead")


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def draw_health_bar(self, surface):
        health_bar_length = 50
        health_ratio = self.health / self.max_health
        health_bar_width = int(health_bar_length * health_ratio)
        health_bar_color = (0, 255, 0)  # Green for healthy
        pygame.draw.rect(surface, health_bar_color, (self.rect.x, self.rect.y - 10, health_bar_width, 5))