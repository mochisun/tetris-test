import pygame, sys
from grid import Grid

#initialize pygame
pygame.init()

dark_blue = (44, 44, 137)

#create screen for display
screen = pygame.display.set_mode((300, 600))
#caption set
pygame.display.set_caption("PyTetris")

#init a clock for pygame
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

#game run loop
#1. event handling
#2. updating positions
#3. drawing objects
while True:
    for event in pygame.event.get():
        #quit upon exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Drawing
    screen.fill(dark_blue)

    #updates/draws picture of display
    pygame.display.update()
    #number of frames per second for game
    clock.tick(60 )