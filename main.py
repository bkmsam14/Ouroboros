import pygame
import math
import Button
import Character
class GameState:
    MENU = 'menu'
    GAME = 'game'
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Ouroboros")
icon = pygame.image.load("Ouroboros.svg.png")


bg = pygame.image.load("tzKyzs.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

pygame.display.set_icon(icon)
# Load images
unpushed_start_image = pygame.image.load("play_unpushed.png")
pushed_start_image = pygame.image.load("pushed_start.png")
unpushed_quit_image = pygame.image.load("unpushed_quit.png")
pushed_quit_image = pygame.image.load("pushed_quit.png")
character_image = pygame.image.load("character.png")
title = pygame.image.load("title.png")
start_button = Button.Button(320, 300, unpushed_start_image, pushed_start_image, 0.85)
quit_button = Button.Button(620, 309, unpushed_quit_image, pushed_quit_image, 0.83)
character = Character.Character(60, 40, 5,character_image,0.2)
current_game_state = GameState.MENU


running = True
while running:

    clock.tick(FPS)
    if current_game_state == GameState.MENU:

        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll

        scroll -= 1
        if abs(scroll) > bg_width:
            scroll = 0
        screen.blit(title, (360, 50))
        action1 = start_button.draw(screen)
        action2 = quit_button.draw(screen)

        if action1:
            current_game_state = GameState.GAME
        if action2:
            running = False
    elif current_game_state == GameState.GAME:
            character.move(keys)
            screen.fill((211, 211, 211))
            character.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    keys = pygame.key.get_pressed()
    pygame.display.flip()
pygame.quit()