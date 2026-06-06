import sys
import pygame
from classes.Enemy import Enemy
from classes.Player import Player

pygame.init()

sound_ball = pygame.mixer.Sound('Sounds/effect_ball.mp3')

SCREEN_W, SCREEN_H = 800, 600
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
background = pygame.transform.scale(pygame.image.load("images/background.jpg"), (SCREEN_W, SCREEN_H))
pygame.display.set_caption("Ping-Pong")

player1 = Player("images/platform.png", 107, 408, 0, 4, 40, 200)
player2 = Player("images/platform_enemy.png", 107, 408, 0, 4, 735, 200)
player1.change_size_factor(0.3)
player2.change_size_factor(0.3)
player1.reset()
player2.reset()

ball = Enemy('images/ball.png', 224, 224, 0, 3, (400, 500), end_pos=None)
ball.change_size_factor(0.3)

win_blue = Enemy('images/win_blue.png', 579, 563, 0, 0, (400, 260), end_pos=None)
win_red = Enemy('images/win_red.png', 685, 642, 0, 0, (400, 260), end_pos=None)
win_blue.change_size_factor(0.5)
win_red.change_size_factor(0.5)

fps = 60
clock = pygame.time.Clock()
can_collide = True

while True:
    clock.tick(fps)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.rect.top > 0:
        player1.rect.y -= player1.speed
    if keys[pygame.K_s] and player1.rect.bottom < SCREEN_H:
        player1.rect.y += player1.speed

    if keys[pygame.K_UP] and player2.rect.top > 0:
        player2.rect.y -= player2.speed
    if keys[pygame.K_DOWN] and player2.rect.bottom < SCREEN_H:
        player2.rect.y += player2.speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.rect.x += ball.speedx
    ball.rect.y += ball.speedy
    if ball.collide(player2.rect) and can_collide == True:
        ball.speedx *= -1
        can_collide = False
        sound_ball.play()

    if ball.collide(player1.rect) and can_collide == False:
        ball.speedx *= -1
        can_collide = True
        sound_ball.play()

    if ball.rect.y >= SCREEN_H-35 or ball.rect.y <= 0:
        ball.speedy *= -1

    if ball.rect.x >= SCREEN_W-35:
        window.blit(win_blue.image, win_blue.rect)
        break

    if ball.rect.x <= 0:
        window.blit(win_red.image, win_red.rect)
        break

    window.blit(background, (0, 0))
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)
    window.blit(ball.image, ball.rect)

    pygame.display.flip()

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()