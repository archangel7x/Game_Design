import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
ORIGINAL_WIDTH, ORIGINAL_HEIGHT = 600, 600
FPS = 120

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Calculate aspect ratio
ASPECT_RATIO = ORIGINAL_WIDTH / ORIGINAL_HEIGHT

# Get the screen's width and height
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Calculate new width and height based on aspect ratio
if SCREEN_WIDTH / SCREEN_HEIGHT > ASPECT_RATIO:
    NEW_WIDTH = int(SCREEN_HEIGHT * ASPECT_RATIO)
    NEW_HEIGHT = SCREEN_HEIGHT
else:
    NEW_WIDTH = SCREEN_WIDTH
    NEW_HEIGHT = int(SCREEN_WIDTH / ASPECT_RATIO)

# Center the game window
X_OFFSET = (SCREEN_WIDTH - NEW_WIDTH) // 2
Y_OFFSET = (SCREEN_HEIGHT - NEW_HEIGHT) // 2

# Create the game window
screen = pygame.display.set_mode((NEW_WIDTH, NEW_HEIGHT))

pygame.display.set_caption("Pac-Man Game")
clock = pygame.time.Clock()

# Pac-Man attributes
pacman_radius = int(NEW_WIDTH / 20)  # Adjust the size relative to the new window size
pacman_x = NEW_WIDTH // 2
pacman_y = NEW_HEIGHT // 2
pacman_direction = 0  # 0: right, 1: up, 2: left, 3: down

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
        pacman_x += int(NEW_WIDTH / 100)  # Adjust the movement speed relative to the new window size
    elif keys[pygame.K_UP]:
        pacman_direction = 1
        pacman_y -= int(NEW_HEIGHT / 100)
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
        pacman_x -= int(NEW_WIDTH / 100)
    elif keys[pygame.K_DOWN]:
        pacman_direction = 3
        pacman_y += int(NEW_HEIGHT / 100)
    else:
        if keys[pygame.K_x]:
            pygame.quit()
            sys.exit()

    # Draw the background
    screen.fill(BLACK)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    pygame.draw.circle(screen, BLACK, (pacman_x, pacman_y), int(pacman_radius - 0.1 * pacman_radius))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
