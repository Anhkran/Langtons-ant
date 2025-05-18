from .variables import *

class Ant:
    def __init__(self, screen, grid, row, column):

        self.row = row
        self.column = column
        #self.row = SQUARES // 2
        #self.column = SQUARES // 2


        self.direction = 90
        self.grid = grid
        self.screen = screen
    
    def flip(self, num):
        if num == 1:
            return 0
        return 1

    def check_even(self, num):
        if num == 0:
            return True
        elif num < 0:
            return False
        return True

    def reset_to_middle(self):

        for row in range(SQUARES):
            for column in range(SQUARES):
                self.grid[row][column] == 0
        self.row = SQUARES // 2
        self.column = SQUARES // 2

    def check(self):
        
        temp_row = self.row
        temp_column = self.column
        
        try:
            num = self.grid[self.row][self.column]
        except IndexError:
            self.reset_to_middle()
            temp_row = self.row
            temp_column = self.column
            num = self.grid[self.row][self.column]

        if num == 0:
    
            self.grid[self.row][self.column] = self.flip(num)
            self.row = temp_row
            if self.direction != 270:
                self.direction = self.direction + 90
            else:
                self.direction = 0
            self.move()

        else:
            self.grid[self.row][self.column] = self.flip(num)
            self.row = temp_row
            if self.direction != 0:
                self.direction = self.direction - 90
            else:
                self.direction = 270
            self.move()

    def move(self):

        if self.direction == 0:
            if self.check_even(self.column):
                self.column = self.column -1
            else:
                self.direction = 180

        elif self.direction == 90:
            if self.check_even(self.row):
                self.row = self.row -1
            else:
                self.direction = 270

        elif self.direction == 180:
            self.column = self.column + 1
        elif self.direction == 270:
            self.row = self.row + 1

    def draw(self):
        return (self.row, self.column)


