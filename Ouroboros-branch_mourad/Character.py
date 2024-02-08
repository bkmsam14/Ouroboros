import pygame
class Character:
    def __init__(self,x,y,speed,max_health,image,scale):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.vect=pygame.math.Vector2(0,0)
        self.max_health = max_health
        self.health = max_health
        self.immunity = False
        self.immunity_event = pygame.USEREVENT + 1
    
    def move(self, keys):
        if keys[pygame.K_q] and self.rect.x - self.speed > 0:
            self.vect.x=-1
        if keys[pygame.K_d] and self.rect.x + self.speed < 1040 - self.rect.width:
            self.vect.x=1
        if keys[pygame.K_z] and self.rect.y - self.speed > 0:
            self.vect.y=-1
        if keys[pygame.K_s] and self.rect.y + self.speed < 620 - self.rect.height:
            self.vect.y=1
        if self.vect.magnitude()!=0:
            self.vect.normalize_ip()
            self.vect.scale_to_length(self.speed)
        self.rect.center=(self.rect.center[0]+self.vect.x, self.rect.center[1]+ self.vect.y)

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

    def get_health_ratio(self):
        return self.health / self.max_health