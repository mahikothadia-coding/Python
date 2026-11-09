import pygame
import random

pygame.init()

sce = pygame.USEREVENT + 1
bce = pygame.USEREVENT + 2

B1 = pygame.Color("blue")
B2 = pygame.Color("lightblue")
B3 = pygame.Color("darkblue")

S1 = pygame.Color("yellow")
S2 = pygame.Color("magenta")
S3 = pygame.Color("orange")
S4 = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[1]
            boundary-hit == True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sce))
            pygame.event.post(pygame.event.Event(bce))
    def change_color(self):
        self.image.fill(random.choice([S1,S2,S3,S4]))
def change_background_color():
    global bg_color
    bg_color = random.choice([B1,B2,B3])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(S4 , 20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Boundary Sprite")
bg_color = B1
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock

while not exit:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            exit =True
        elif event.type == sce:
            sp1.change_color()
        elif event.type == bce:
            change_background_color()

        all_sprites_list.update()
        screen.fill(bg_color)
        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(240)

    pygame.quit()                


