from turtle import width

import pygame
import math
import Button
import Character
import Mob
import random

####CAPITAL LETTER VARIABLE NAMES ==> CONSTANTS####

class GameState:
    MENU = 'menu'
    GAME = 'game'
    GAME_OVER = 'game_over'

def character_animation_method(keys,FRAME_CHANGE):
        ###BASIC MOVEMENT###
        global character_index, character_image, character_direction
        if keys[pygame.K_s] ==True:
            character_direction=0
            character_index+=FRAME_CHANGE
            if int(character_index)>= len(character_anim[0]):
                character_index=1
            running_music.play()
        elif keys[pygame.K_z]:
            character_direction=1
            character_index+=FRAME_CHANGE
            if int(character_index)>= len(character_anim[0]):
                character_index=1
            running_music.play()
        elif keys[pygame.K_q]:
            character_direction=2
            character_index+=FRAME_CHANGE
            if int(character_index)>= len(character_anim[0]):
                character_index=1
            running_music.play()
        elif keys[pygame.K_d]:
            character_direction=3
            character_index+=FRAME_CHANGE
            if int(character_index)>= len(character_anim[0]):
                character_index=1  
            running_music.play()
        ### OTHER ANIMATIONS (TEST) ###
        character_image=character_anim[character_direction][int(character_index)]

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 620
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen = pygame.display.get_surface()



pygame.display.set_caption("Ouroboros")
icon = pygame.image.load("Ouroboros.svg.png")


bg = pygame.image.load("Menu-Pictures/menu1.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()


##CONSTANT LISTS FOR ANIMATION##
CHARACTER_RESTDOWN=pygame.image.load("Test-Character/atRestDOWN.png").convert_alpha()
CHARACTER_MOVE1DOWN=pygame.image.load("Test-Character/movingFrame1DOWN.png").convert_alpha()
CHARACTER_MOVE2DOWN=pygame.image.load("Test-Character/movingFrame2DOWN.png").convert_alpha()

CHARACTER_RESTUP=pygame.image.load("Test-Character/atRestUP.png").convert_alpha()
CHARACTER_MOVE1UP=pygame.image.load("Test-Character/movingFrame1UP.png").convert_alpha()
CHARACTER_MOVE2UP=pygame.image.load("Test-Character/movingFrame2UP.png").convert_alpha()

CHARACTER_RESTRIGHT=pygame.image.load("Test-Character/atRestRIGHT.png").convert_alpha()
CHARACTER_MOVE1RIGHT=pygame.image.load("Test-Character/movingFrame1RIGHT.png").convert_alpha()
CHARACTER_MOVE2RIGHT=pygame.image.load("Test-Character/movingFrame2RIGHT.png").convert_alpha()

CHARACTER_RESTLEFT=pygame.image.load("Test-Character/atRestLEFT.png").convert_alpha()
CHARACTER_MOVE1LEFT=pygame.image.load("Test-Character/movingFrame1LEFT.png").convert_alpha()
CHARACTER_MOVE2LEFT=pygame.image.load("Test-Character/movingFrame2LEFT.png").convert_alpha()

CHARACTER_CHANGE=pygame.image.load("character.png").convert_alpha()

character_anim=[[CHARACTER_RESTDOWN, CHARACTER_MOVE1DOWN, CHARACTER_MOVE2DOWN],
                [CHARACTER_RESTUP, CHARACTER_MOVE1UP, CHARACTER_MOVE2UP],
                [CHARACTER_RESTLEFT, CHARACTER_MOVE1LEFT, CHARACTER_MOVE2LEFT],
                [CHARACTER_RESTRIGHT, CHARACTER_MOVE1RIGHT, CHARACTER_MOVE2RIGHT]]
FRAME_CHANGE=0.08
character_index=0
character_direction=0



pygame.display.set_icon(icon)
# Load images
unpushed_start_image = pygame.image.load("Menu-Pictures/play-export.png")
pushed_start_image = pygame.image.load("Menu-Pictures/play-export.png") ##IN NEED OF CHANGE
unpushed_quit_image = pygame.image.load("Menu-Pictures/quit-export.png")
pushed_quit_image = pygame.image.load("Menu-Pictures/quit-export.png") ##IN NEED OF CHANGE
character_image = character_anim[character_direction][character_index]
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (20, 20))
mob_image = pygame.image.load("mob.png")
start_button = Button.Button(145, 130, unpushed_start_image, pushed_start_image, 0.85)
quit_button = Button.Button(665, 130, unpushed_quit_image, pushed_quit_image, 0.83)
character_scale=0.2
character = Character.Character(60, 40, 3, 10,character_image,character_scale)
current_game_state = GameState.MENU
mobs = [Mob.Mob(x=random.randint(0, 800), y=random.randint(0, 600), speed=2, image=mob_image, max_health=10, scale=0.1) for _ in range(5)]


### SAMPLE MUSIC ###
intro=pygame.mixer.Sound('Music/intro-music.mp3')
running_music=pygame.mixer.Sound('Music/running.wav')



running = True
while running:

    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    if current_game_state == GameState.MENU:
        intro.play()
        screen.blit(pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        action1 = start_button.draw(screen)
        action2 = quit_button.draw(screen)
        if action1:
            current_game_state = GameState.GAME
        if action2:
            running = False
    elif current_game_state == GameState.GAME:
        intro.stop()
        character.move(keys)
        character_animation_method(keys, FRAME_CHANGE)
        character.image=pygame.transform.scale(character_image, (int(character_image.get_width() * character_scale), int(character_image.get_height() * character_scale))).convert_alpha()
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
        heart_spacing = 25
        for i in range(character.health):
            screen.blit(heart_image, (10 + i * heart_spacing, 10))

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
        if event.type==pygame.KEYUP:
            character.vect.x=0
            character.vect.y=0
            character_index=0
            character_image=character_anim[character_direction][int(character_index)]
            character.image=pygame.transform.scale(character_image, (int(character_image.get_width() * character_scale), int(character_image.get_height() * character_scale))).convert_alpha()
            running_music.stop()
    pygame.display.update()
    pygame.display.flip()

pygame.quit()