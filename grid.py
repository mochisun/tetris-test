class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        #list comprehension -> shorthand way to create lists
        self.grid = [[0 for j in range(self.num_cols)] for i in range (self.num_rows)]
        



    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end = " ")
            print()  
    
    def get_cell_colors(self):
        return