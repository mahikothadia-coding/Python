"""Activity 3: color changing sprite
WHAT YOU WILL BUILD
You build a Pygame sprite that moves with the arrow keys and changes color whenever it touches a screen edge.
HOW IT WORKS
• Step 1: Define a main() function, initialize pygame, and create a 500x500 window with a caption.
• Step 2: Store five named colors in a colors dictionary, and set current_color to white.
• Step 3: Set the sprite's starting x, y position and its width and height, then create a clock to control frame rate.
• Step 4: Start the main loop, checking pygame.event.get() for the pygame.QUIT event.
• Step 5: Call pygame.key.get_pressed() and use four if checks on the arrow keys to adjust x and y.
• Step 6: Clamp x and y with min() and max() so the sprite stays fully inside the screen.
• Step 7: Use an if/elif chain on x and y to set current_color whenever the sprite touches an edge.
• Step 8: Fill the screen black, draw the sprite rectangle in current_color, flip the display, and tick the clock.
Remember
These three activities combine every topic learned in this lesson - drawing shapes with pygame.Rect, solid versus outlined shapes, and reading, moving, clamping, and coloring a sprite with the keyboard.
"""
"""DONE WITH THE HELP OF PAPA"""

import pygame
# • Step 1: Define a main() function, initialize pygame, and create a 500x500 window with a caption.
pygame.init()
window1 = pygame.display.set_mode((500,500))
window_caption = "Colour changing sprites"
pygame.display.set_caption(window_caption)
def main():
    # • Step 2: Store five named colors in a colors dictionary, and set current_color to white.
    color_dictionary = {
        "red": pygame.Color(255, 0, 0),
        "blue": pygame.Color(0, 0, 255),
        "green": pygame.Color(0, 255, 0),
        "yellow": pygame.Color(255, 255, 0),
        "brown": pygame.Color(139, 69, 19)
    }
    current_color = pygame.Color(255,255,255)
    # • Step 3: Set the sprite's starting x, y position and its width and height, then create a clock to control frame rate.
    s_left = 225
    s_top = 225
    s_width = 80
    s_height = 80
    sprite = pygame.Rect(s_left, s_top, s_width, s_height)
    clock = pygame.time.Clock()
    # • Step 4: Start the main loop, checking pygame.event.get() for the pygame.QUIT event.

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # • Step 5: Call pygame.key.get_pressed() and use four if checks on the arrow keys to adjust x and y.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            s_left -= 5
        if keys[pygame.K_RIGHT]:
            s_left += 5
        if keys[pygame.K_UP]:
            s_top -= 5
        if keys[pygame.K_DOWN]:
            s_top += 5
        # • Step 6: Clamp x and y with min() and max() so the sprite stays fully inside the screen.
        s_left = max(0, min(s_left, 500 - s_width))
        s_top = max(0, min(s_top, 500 - s_height))
        # • Step 7: Use an if/elif chain on x and y to set current_color whenever the sprite touches an edge.
        if s_left == 0:
            current_color = color_dictionary["red"]
        elif s_left == 500 - s_width:
            current_color = color_dictionary["blue"]
        elif s_top == 0:
            current_color = color_dictionary["green"]
        elif s_top == 500 - s_height:
            current_color = color_dictionary["yellow"]
        # • Step 8: Fill the screen black, draw the sprite rectangle in current_color, flip the display, and tick the clock.
        window1.fill((0,0,0))
        pygame.draw.rect(window1,current_color, (s_left, s_top, s_width, s_height))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()