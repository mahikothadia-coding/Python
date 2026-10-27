"""Activity 2: Hollow and Solid Ball
WHAT YOU WILL BUILD
You build a Pygame window with two green circles, one solid and one hollow, on a white background.
HOW IT WORKS
• Step 1: Import pygame and call pygame.init() to start it up.
• Step 2: Create a 400x400 display window using pygame.display.set_mode() and store it in window.
• Step 3: Fill the window with white using window.fill((255, 255, 255)).
• Step 4: Store the color green in a variable named GREEN.
• Step 5: Draw a solid circle with pygame.draw.circle(window, GREEN, (300, 300), 50).
• Step 6: Draw a hollow circle with pygame.draw.circle(window, GREEN, (100, 100), 50, 3), using width 3 for the outline.
• Step 7: Call pygame.display.update() to show both circles, then run an event loop that quits when the window closes.
"""

# • Step 1: Import pygame and call pygame.init() to start it up.
import pygame
pygame.init()
# • Step 2: Create a 400x400 display window using pygame.display.set_mode() and store it in window.
window = pygame.display.set_mode((400,400))
# • Step 3: Fill the window with white using window.fill((255, 255, 255)).
window.fill((255,255,255))
# • Step 4: Store the color purple in a variable named Purple.
purple = (120, 95, 196)
# • Step 5: Draw a solid circle with pygame.draw.circle(window, GREEN, (300, 300), 50).
solid_circle = pygame.draw.circle(window, purple,(300,300),50)
    
# • Step 6: Draw a hollow circle with pygame.draw.circle(window, GREEN, (100, 100), 50, 3), using width 3 for the outline.
hollow_circle = pygame.draw.circle(window, purple, (100,100), 50, 3)

# • Step 7: Call pygame.display.update() to show both circles, then run an event loop that quits when the window closes.
pygame.display.update()

def game_loop() :
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # solid_circle
        # hollow_circle
        # show_circles 
           
    # pygame.quit()

if __name__ == "__main__":
    game_loop()








