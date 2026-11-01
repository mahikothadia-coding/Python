# Step 1: Create the Pygame Screen Create a new Python file. Import pygame, initialize
# it, and create a screen using pygame.display.set_mode(). Add a caption for the game
# window.
import pygame
def main():
    pygame.init()
screen_width = 500
screen_height = 500    
screen = pygame.display.set_mode((screen_height, screen_width))    
pygame.display.set_caption("Sprite Adventure")
# Step 2: Set the Sprite Position and Size Create x and y variables for the sprite
# position. Also create sprite_width, sprite_height, and speed so the rectangle can be
# drawn and moved.
sprite_x = 50
sprite_y = 50
sprite_width = 80
sprite_height = 80
speed = 8
# Step 3: Define Colors Create color variables using RGB values. These colors will be
# used for the background, circles, and moving sprite.
white = (0,0,0)
pink = (255, 192, 203)
purple = (177, 156, 217)
blue = (167, 199, 231)
yellow = (255, 238, 140)
green = (119, 221, 119)
current_colour = white
clock = pygame.time.Clock()
# Step 4: Create the Game Loop Use a while loop so the game window stays open until
# the player closes it. Handle pygame.QUIT inside the event loop.
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
# Step 5: Check Arrow Keys with get_pressed() Use pygame.key.get_pressed() to
# check which arrow keys are being held down. Update x and y when the user presses
# left, right, up, or down.
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

# Step 6: Keep the Sprite Inside the Screen Use min() and max() to stop the sprite from
# moving outside the screen boundaries.
x = min(max(0,sprite_x), screen_width - sprite_width)
y = min(max(0, sprite_y), screen_height - sprite_height)
# Step 7: Change Color Based on Position Use if, elif, and else statements to change
# the sprite color when it touches the left, right, top, or bottom edge.
    
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

# Step 8: Draw Shapes and Sprite Fill the screen with a background color, draw one
# solid circle and one outlined circle, then draw the moving rectangle using pygame.Rect.
screen.fill(green)
# Step 9: Run and Explore Run the program and move the sprite using arrow keys.
# Touch each edge of the screen and observe how the sprite color changes.
    # PART 9: Draw solid and outlined shapes
pygame.draw.circle(screen, green, (420, 320), 35)
pygame.draw.circle(screen, blue, (80, 320), 35, 4)
    # PART 10: Draw the moving sprite using pygame.Rect
sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
pygame.draw.rect(screen, current_color, sprite_rect)
pygame.display.flip()
clock.tick(80)
pygame.quit()
if __name__ == "__main__":