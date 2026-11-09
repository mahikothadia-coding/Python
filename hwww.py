
import pygame
def main():
    pygame.init()
    screen_width = 500
    screen_height = 500    
    screen = pygame.display.set_mode((screen_height, screen_width))    
    pygame.display.set_caption("Sprite Adventure")
    sprite_x = 50
    sprite_y = 50
    sprite_width = 80
    sprite_height = 80
    speed = 8

    white = (0,0,0)
    pink = (255, 192, 203)
    purple = (177, 156, 217)
    blue = (167, 199, 231)
    yellow = (255, 238, 140)
    green = (119, 221, 119)
    current_colour = white
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_x = -5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sprite_x = 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_y += 5
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        sprite_y -= 5          
    x = min(max(0,sprite_x), screen_width - sprite_width)
    y = min(max(0, sprite_y), screen_height - sprite_height)
    if x == 0:
        current_color = purple
    elif x == screen_width - sprite_width:
        current_color = yellow
    elif y == 0:
        current_color = pink
    elif y == screen_height - sprite_height:
        current_color = blue
    else:
        current_color = green

    screen.fill(green)
    pygame.draw.circle(screen, green, (420, 320), 35)
    pygame.draw.circle(screen, blue, (80, 320), 35, 4)
    sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
    pygame.draw.rect(screen, current_color, sprite_rect)
    pygame.display.flip()
    clock.tick(80)
pygame.quit()
if __name__ == "__main__":
    main()