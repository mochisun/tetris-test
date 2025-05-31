import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        #list comprehension -> shorthand way to create lists
        self.grid = [[0 for j in range(self.num_cols)] for i in range (self.num_rows)]
        self.colors = Colors.get_cell_colors()


    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end = " ")
            print()  
    

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                #get value (0-7)
                cell_value = self.grid[row][col]
                #set up a rectangle for this coordinate (+1/-1 for offset of rect instead of completely filling area)
                cell_rect = pygame.Rect(col*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                #draw the rect with all info
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)