import math
import random
import pygame

s_w = 800
s_h = 500
player_start_x = 370
playe_start_y = 380
e_s_y_min = 50
e_s_x__max = 150
e_s_x = 4
e_s_y = 40
b_s_y = 10
c_d = 27

pygame.init()

screen = pygame.dislpay.set_mode((s_w , s_h))

backgound = pygame.image.load("background.png")

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerx = player_start_x
playery = playe_start_y
playerx_change = 0 

enemyImg = []
enemyx = []
enemyy = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 6

for _i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randit(0,s_w - -64))

    enemyy.append(random.randit(e_s_y_min, e_s_x__max))
    enemy_x_change.append(e_s_x)
    enemy_y_change.append(e_s_y)

bulletImg = pygame.image.load("bullet.png")
bulletx = 0
bullety = playe_start_y
bulletx_change = 0
bullety_change = b_s_y
bullet_state = "ready"

score_value = 0 
font = pygame.font.Font("freesansbold.ttf" , 32)
textx = 10
texty = 10

over_font = pygame.font.Font("freesansbold.ttf" , 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value) , True,(255,255,255))
    screen.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("Game Over!!" , True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(playerImg , (x, y))


