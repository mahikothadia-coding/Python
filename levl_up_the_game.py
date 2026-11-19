import pygame
import random

sw , sh = 500,400
movement_speed = 5
font_size = 72

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.png"),(sw,sh))

font = pygame.font.SysFont("Times New Roman", font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color , height , width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x= max(min(self.rect.x + x_change, sw - self.rect.width),0)
        self.rect.y= max(min(self.rect.y + y_change, sh - self.rect.height),0)

screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Sprite Collision")
a_s = pygame.sprite.Group()

s1 = Sprite(pygame.Color("pink"), 20, 30)
s1.rect.x,s1.rect.y = random.randint(0, sw - s1.rect.width),random.randint(0, sh, - s1.rect.height)
a_s.add(s1)

s2 = Sprite(pygame.Color("white"), 20, 30)
s2.rect.x,s2.rect.y = random.randint(0, sw - s2.rect.width),random.randint(0, sh, - s2.rect.height)
a_s.add(s2)

running, won = True ,False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type ==  pygame.KEYDOWN
                                         and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] -keys[pygame.K_UP]) * movement_speed
        s1.move(x_change, y_change)

        if s1.rect.colliderect(s2.rect):
            a_s.remove(s2)
            won = True
        screen.blit(background_image, (0,0))
        a_s.draw(screen)
    if won:
        win_text = font.render("You Win!!" , True,pygame.Color("black"))
        screen.blit(win_text, ((sw - win_text.get_width))) // 2,
        screen.blit(win_text, ((sh - win_text.get_height))) // 2,
    pygame.display.flip()
    clock.tick(90)
pygame.quit()    

                    
