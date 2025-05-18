import pygame
from bin.variables import *
from bin.ant import *

pygame.init()
pygame.display.set_caption('Ant test')

clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))


grid = []
for row in range(SQUARES):
    grid.append([])
    for column in range(SQUARES):
        grid[row].append(0)

ant = Ant(screen, grid, 160, 160)
calc = MARGIN + SIZE

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ro, col = ant.draw()
    for row in range(SQUARES):
        for column in range(SQUARES):
            if grid[row][column] == 1:
                color = blue_color
            else:
                color = gray_color
            pygame.draw.rect(screen,
                             color,
                             [calc * column + MARGIN,
                              calc * row + MARGIN,
                              SIZE,
                              SIZE])

            pygame.draw.rect(screen, ant_color,
                            [calc * col + MARGIN,
                            calc * ro + MARGIN,
                            SIZE,
                            SIZE])

    ant.check()
    pygame.display.update()
    clock.tick(FRAMELIMIT)

pygame.quit()

