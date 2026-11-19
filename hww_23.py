import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Add more Sprites")
background = pygame.image.load("background.png")
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
font = pygame.font.Font("freesansbold.ttf", 32)


pX = 370
pY = 380
pX_change = 0
pY_change = 0
score = 0


num_of_e = 7
eX = []
eY = []
for i in range(num_of_e):
    eX.append(random.randint(0, 736))
    eY.append(random.randint(50, 400))



def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance < 40


running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -5
            if event.key == pygame.K_RIGHT:
                pX_change = 5
            if event.key == pygame.K_UP:
                pY_change = -5
            if event.key == pygame.K_DOWN:
                pY_change = 5
        if event.type == pygame.KEYUP:
            pX_change = 0
            pY_change = 0

    pX += pX_change
    pY += pY_change
    pX = max(0, min(pX, 736))
    pY = max(0, min(pY, 436))

    for i in range(num_of_e):
        if isCollision(pX, pY, eX[i], eY[i]):
            score += 1
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 400)
        screen.blit(enemyImg, (eX[i], eY[i]))

    screen.blit(playerImg, (pX, pY))
    screen.blit(font.render("Score : " + str(score), True, (255, 255, 255)), (10, 10))
    pygame.display.update()
