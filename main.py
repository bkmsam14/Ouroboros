from turtle import width

import pygame
import math
import Button
import Character
import Mob
import random
class GameState:
    MENU = 'menu'
    GAME = 'game'
    GAME_OVER = 'game_over'
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 620
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
mob_image = pygame.image.load("mob.png")
title = pygame.image.load("title.png")
start_button = Button.Button(260, 300, unpushed_start_image, pushed_start_image, 0.85)
quit_button = Button.Button(560, 309, unpushed_quit_image, pushed_quit_image, 0.83)
character = Character.Character(60, 40, 5,10,character_image,0.2)
current_game_state = GameState.MENU
mobs = [Mob.Mob(x=random.randint(0, 800), y=random.randint(0, 600), speed=2, image=mob_image, max_health=10, scale=0.1) for _ in range(5)]


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
        screen.blit(title, (300, 50))
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
        for mob in mobs:
            mob.update()
            mob.draw(screen)
            mob.draw_health_bar(screen)
            if character.rect.colliderect(mob.rect):
                character.take_damage(1)
        character.draw_health_bar(screen)
        if character.health <= 0:
            current_game_state = GameState.GAME_OVER
    elif current_game_state == GameState.GAME_OVER:
        # Display "You Died" message on a black screen
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("You Died", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_game_state == GameState.GAME and event.type == character.immunity_event:
            print('not immune')
            character.immunity = False

    pygame.display.update()
    keys = pygame.key.get_pressed()
    pygame.display.flip()

pygame.quit()