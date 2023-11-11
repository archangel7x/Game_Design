import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
FPS = 120

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Get the screen's width and height
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Create the game window with the entire screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("Pac-Man Game")
clock = pygame.time.Clock()

# Pac-Man attributes
pacman_radius = int(SCREEN_WIDTH / 20)  # Adjust the size relative to the screen size
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
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
        pacman_x += int(SCREEN_WIDTH / 100)  # Adjust the movement speed relative to the screen size
    elif keys[pygame.K_UP]:
        pacman_direction = 1
        pacman_y -= int(SCREEN_HEIGHT / 100)
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
        pacman_x -= int(SCREEN_WIDTH / 100)
    elif keys[pygame.K_DOWN]:
        pacman_direction = 3
        pacman_y += int(SCREEN_HEIGHT / 100)
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
