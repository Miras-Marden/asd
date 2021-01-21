import pygame
from tkinter import *
import time
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

pygame.font.get_fonts()
pygame.mixer.pre_init(44100, -16, 1, 512)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SILVER = (105, 105, 105)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tennis")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 690
paddleB.rect.y = 200

ball = Ball(RED, 20, 20)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

counter = 0

pygame.font.init()
myFont = pygame.font.SysFont('hooge 05_53', 65)
smallFont = pygame.font.SysFont('hooge 05_53', 20)
Space = pygame.font.SysFont('hooge 05_53', 17)
largeFont = pygame.font.SysFont('hooge 05_53', 85)
largerFont = pygame.font.SysFont('hooge 05_53', 120)


def pause():
    paused = True
    while paused:
        for event_pause in pygame.event.get():
            if event_pause.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_pause.type == pygame.KEYDOWN:
                if event_pause.key == pygame.K_c:
                    paused = False
                elif event_pause.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(BLACK)
        textSurface = largerFont.render('I I', False, (255, 255, 255))
        screen.blit(textSurface, (295, 45))
        textSurface = largeFont.render('PAUSED', False, (255, 255, 255))
        screen.blit(textSurface, (175, 160))
        pygame.draw.rect(screen, SILVER, (219, 280, 260, 60))
        textSurface = smallFont.render('PRESS C TO CONTINUE', False, (255, 255, 255))
        screen.blit(textSurface, (223, 300))

        pygame.display.update()


introOn = True
while introOn:
    screen.fill(BLACK)
    textSurface = largerFont.render('Tennis', False, (255, 255, 255))
    screen.blit(textSurface, (110, 200))
    textSurface = Space.render('[PRESS SPACE TO PLAY!]', False, (255, 255, 255))
    screen.blit(textSurface, (220, 403))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                introOn = False

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
            elif event.key == pygame.K_p:
                pause()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.change_color((255, 255, 255))
        counter = 1

    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.change_color((123, 255, 230))
        counter = 1

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
        ball.change_color((255, 255, 255))
        counter = 1

    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
        ball.change_color((234, 255, 123))
        counter = 1

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
        counter = 1

    if counter > 0:
        counter += 1

    if counter > 10:
        ball.change_color((255, 255, 255))
        counter = 0

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    all_sprites_list.draw(screen)

    player = pygame.font.SysFont("hooge 05_53", 28)
    font = pygame.font.SysFont("hooge 05_53", 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (240, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))
    textSurface = player.render('P1', False, (255, 255, 255))
    screen.blit(textSurface, (85, 15))
    textSurface = player.render('P2', False, (255, 255, 255))
    screen.blit(textSurface, (575, 15))

    pygame.display.flip()

    clock.tick(60)


conclusionOn = True
while conclusionOn:
    screen.fill(BLACK)
    if scoreA > scoreB:
        textSurface = myFont.render('PLAYER 1 WINS!', False, (255, 255, 255))
        screen.blit(textSurface, (58, 200))
    elif scoreA < scoreB:
        textSurface = myFont.render('PLAYER 2 WINS!', False, (255, 255, 255))
        screen.blit(textSurface, (58, 200))
    else:
        textSurface = myFont.render('draw score!', False, (255, 255, 255))
        screen.blit(textSurface, (100, 200))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                conclusionOn = False


pygame.quit()
