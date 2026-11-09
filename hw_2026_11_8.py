import pygame
import random

# • Step 1: Import and Initialize Pygame
pygame.init()

# • Step 2: Create the Custom Event IDs
CAR_COLOUR_CHANGING = pygame.USEREVENT + 1
SIGNAL_COLOUR_CHANGING = pygame.USEREVENT + 2

# • Step 3: Define the Colours
ROAD_COLOUR = pygame.Color("grey")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
PINK = pygame.Color("pink")
PURPLE = pygame.Color("purple")

COLOR_PALETTE = [WHITE, YELLOW, RED, GREEN, PINK, PURPLE]

# • Step 4: Create the Car Sprite Class
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        # • Step 5: Give the Car an Image, Rect, and Velocity
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        # Position the car on the screen
        self.rect.x = 50
        self.rect.y = 200
        
        # Horizontal velocity list [x_speed, y_speed]
        self.velocity = [5, 0]

    # • Step 6: Move the Car and Detect Boundaries
    def update(self):
        self.rect.move_ip(self.velocity)
        sensor_triggered = False
        
        # Reverse horizontal velocity if the car hits the screen edges (500 width)
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            sensor_triggered = True
        
        # • Step 7: Post the Custom Events
        if sensor_triggered: 
            pygame.event.post(pygame.event.Event(CAR_COLOUR_CHANGING))
            pygame.event.post(pygame.event.Event(SIGNAL_COLOUR_CHANGING))

    def change_color(self):
        random_color = random.choice(COLOR_PALETTE)
        self.image.fill(random_color)

# --- Execution Setup & Game Loop ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Simulation")

# Sprite setup
all_sprites = pygame.sprite.Group()
player_car = Car(RED, 60, 30)
all_sprites.add(player_car)

# Traffic Light Setup
signal_color = GREEN

clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CAR_COLOUR_CHANGING:
            player_car.change_color()
        elif event.type == SIGNAL_COLOUR_CHANGING:
            signal_color = random.choice([RED, YELLOW, GREEN])

    # Game logic
    all_sprites.update()

    # Drawing
    screen.fill(ROAD_COLOUR)
    
    # Draw a simple traffic light box and light
    pygame.draw.rect(screen, WHITE, (225, 20, 50, 50))
    pygame.draw.circle(screen, signal_color, (250, 45), 15)
    
    # Draw sprites
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
