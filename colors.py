class Colors:
    #dark grey for normal background color
    dark_grey = (20, 30, 40)
    #other 7 colors for each tetris shape
    green = (50, 230, 20)
    red = (230, 20, 20)
    orange = (230, 120, 20)
    yellow = (240, 240, 4)
    purple = (160, 0, 250)
    cyan = (20, 200, 200)
    blue = (10, 60, 210)

    #python decorator that can be called on a class
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]