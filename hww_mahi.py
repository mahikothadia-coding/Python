# Pet Food Collection Game
import pygame
import random

S_W, S_H = 500, 400
M_S = 5
F_S = 60

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("pet_bg.jpg"), (S_W, S_H))
font = pygame.font.SysFont("Arial", F_S)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(0, min(S_W - self.rect.width, self.rect.x + x_change))
        self.rect.y = max(0, min(S_H - self.rect.height, self.rect.y + y_change))

screen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Pet Food Collection Game")
all_sprites = pygame.sprite.Group()

pet = Sprite(pygame.Color("brown"), 40, 40)
pet.rect.x = 30
pet.rect.y = 180
all_sprites.add(pet)

pet_food = Sprite(pygame.Color("yellow"), 30, 30)
pet_food.rect.x = random.randint(100, S_W - 30)
pet_food.rect.y = random.randint(0, S_H - 30)
all_sprites.add(pet_food)

running = True
food_collected = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not food_collected:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * M_S
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * M_S
        pet.move(x_change, y_change)

        if pet.rect.colliderect(pet_food.rect):
            all_sprites.remove(pet_food)
            food_collected = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if food_collected:
        message = font.render("Food Collected!", True, pygame.Color("black"))
        text_x = (S_W - message.get_width()) // 2
        text_y = (S_H - message.get_height()) // 2
        screen.blit(message, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
