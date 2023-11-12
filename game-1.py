import pygame
import sys
from colour import Color
import random 

# Initialize Pygame
pygame.init()

# Constants
FPS = 120

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
#WHITE= Color("white")
WHITE = (255,255,255)
GREY = (128,128,128)
GREY2=(159,159,159)
GREY3=(189,189,189)
BLUE= (0,0,255)
RED= (255,0,0)
GREEN=(0,255,0)

SHAKE_DURATION = 5
SHAKE_AMOUNT = 2


PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 0, 0
# VARS:
_VARS = {'surf': False}
# Get the screen's width and height
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

SCREENSIZE = SCREEN_WIDTH, SCREEN_HEIGHT 
# Create the game window with the entire screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("Pac-Man Game")
clock = pygame.time.Clock()

# Pac-Man attributes
pacman_radius = int(SCREEN_WIDTH / 50)  # Adjust the size relative to the screen size
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
pacman_direction = 0  # 0: right, 1: up, 2: left, 3: down




score = 0 
char_color = GREY
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


def shake_screen():
    original_position = screen.get_rect().topleft
    for _ in range(SHAKE_DURATION):
        dx, dy = random.randint(-SHAKE_AMOUNT, SHAKE_AMOUNT), random.randint(-SHAKE_AMOUNT, SHAKE_AMOUNT)
        screen.blit(_VARS['surf'], (dx, dy))
        pygame.display.flip()
        pygame.time.delay(1)
        screen.blit(_VARS['surf'], original_position)
        pygame.display.flip()


def show_score(x,y,score):
    
    showing = font.render("Score: "+ str(score),True, (255,255,255))
    screen.blit(showing,(x, y))
    
    

# Main game loop
def drawRect():
    # There's a native way to draw a rectangle in pygame,
    # this is just to explain how lines can be drawn.
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (SCREEN_WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)
    # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, SCREEN_HEIGHT - PADTOPBOTTOM),
      (SCREEN_WIDTH - PADLEFTRIGHT, SCREEN_HEIGHT - PADTOPBOTTOM), 2)
    # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (0 + PADLEFTRIGHT, SCREEN_HEIGHT - PADTOPBOTTOM), 2)
    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (SCREEN_WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (SCREEN_WIDTH - PADLEFTRIGHT, SCREEN_HEIGHT - PADTOPBOTTOM), 2)



_VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
_VARS['surf'].fill(GREY)
drawRect() 

 
class falling:
    def __init__(self):
        #self.size = random.randint(10,50)
        self.size = 10
        #self.color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        self.color =random.choice([BLUE,RED,GREEN])
        self.x = random.randint(PADLEFTRIGHT,SCREEN_WIDTH - PADLEFTRIGHT)
        self.y = 0
 
    def update(self):
        self.y +=5
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.size)
      
      
falling_shapes = []  
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Pac-Man
 
    
    keys = pygame.key.get_pressed()
    pygame.display.update()
    speed = 100
    
    old_pacman_x, old_pacman_y = pacman_x, pacman_y
    

    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
        pacman_x += int(SCREEN_WIDTH / speed)  # Adjust the movement speed relative to the screen size
        #pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
        #print("right")

    elif keys[pygame.K_UP]:
        pacman_direction = 1
        pacman_y -= int(SCREEN_HEIGHT / speed)
        #print("up")

        
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
        pacman_x -= int(SCREEN_WIDTH / speed)
        #print("left")

    elif keys[pygame.K_DOWN]:
        pacman_direction = 3
        pacman_y += int(SCREEN_HEIGHT / speed)
        #print("down")

    else:
        if keys[pygame.K_x]:
            pygame.quit()
            sys.exit()
        
    
    for shape in falling_shapes:
        shape.update()    
     

    # Generate new falling shapes randomly
    if random.randint(0, 100)<5:  # Adjust the probability as needed
        falling_shapes.append(falling())

    # Draw the background
    screen.fill(GREY3)
    show_score(textX,textY,score)
    drawRect()
    
   
        
    for shape in falling_shapes:
        shape.draw(screen)
        
        
    for shape in falling_shapes:
        distance = ((pacman_x - shape.x) ** 2 + (pacman_y - shape.y) ** 2) ** 0.5
        if distance < pacman_radius + shape.size:
            if char_color == shape.color:
                score += 1
                
               #  print("Score:", score)
            else:
                score -=1 
                
                # print("Death")

            falling_shapes.remove(shape)
            shake_screen()
            # Update the display

    if (pacman_x - pacman_radius <PADLEFTRIGHT or pacman_x + pacman_radius > SCREEN_WIDTH - PADLEFTRIGHT or pacman_y - pacman_radius < PADTOPBOTTOM or pacman_y + pacman_radius >SCREEN_HEIGHT - PADTOPBOTTOM):
        pacman_x, pacman_y = old_pacman_x, old_pacman_y
        #pygame.quit()
        #sys.exit()
        
  
   
    # Drawing of the sprites
    if random.randint(1,200) == 1:
        #char_color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        char_color = random.choice([BLUE,RED,GREEN])
    
    
    pygame.draw.circle(screen, BLACK, (pacman_x, pacman_y), pacman_radius)
    pygame.draw.circle(screen, char_color, (pacman_x, pacman_y), int(pacman_radius - 0.1 * pacman_radius))
    
    
    

        
    falling_shapes = [shape for shape in falling_shapes if shape.y < SCREEN_HEIGHT]

    pygame.display.flip()
    
    
        

    # Cap the frame rate
    clock.tick(FPS)
