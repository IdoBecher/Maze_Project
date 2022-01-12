import pygame
import time
import random


# Define colours
WHITE = (255, 255, 255)
BLUE = (155, 155, 255)
YELLOW = (255, 255, 0)


# Set up pygame window
WIDTH = 440
HEIGHT = 440

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze solver")


# Setup maze variables
grid = []
visited = []
stack = []
solution = {}


# Build the grid
z = 20   # width of a cell
for i in range(1, 21):
    for j in range(1, 21):
        grid.append((z*j, z*i))


def go_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - z + 1, 19, 39))
    pygame.display.update()


def go_down(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 19, 39))
    pygame.display.update()


def go_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - z + 1, y + 1, 39, 19))
    pygame.display.update()


def go_right(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 39, 19))
    pygame.display.update()


def current_cell(x, y):
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, 18, 18))
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18))
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x + 8, y + 8, 5, 5))
    pygame.display.update()


def build_and_solve_maze(x, y):
    current_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while stack:
        time.sleep(.11)
        steps = []
        if (x + z, y) not in visited and (x + z, y) in grid:
            steps.append("right")

        if (x - z, y) not in visited and (x - z, y) in grid:
            steps.append("left")

        if (x, y + z) not in visited and (x, y + z) in grid:
            steps.append("down")

        if (x, y - z) not in visited and (x, y - z) in grid:
            steps.append("up")

        if len(steps) > 0:
            next_cell = (random.choice(steps))
            if next_cell == "right":
                go_right(x, y)
                solution[(x + z, y)] = x, y
                x = x + z
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "left":
                go_left(x, y)
                solution[(x - z, y)] = x, y
                x = x - z
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "down":
                go_down(x, y)
                solution[(x, y + z)] = x, y
                y = y + z
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "up":
                go_up(x, y)
                solution[(x, y - z)] = x, y
                y = y - z
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            current_cell(x, y)
            time.sleep(.06)
            backtracking_cell(x, y)


def get_solution(x, y):
    solution_cell(x, y)
    count = 0
    while (x, y) != (20, 20):
        x, y = solution[x, y]
        solution_cell(x, y)
        time.sleep(.2)
        print(x, y)
        count += 1
    return count


build_and_solve_maze(20, 20)
len_of_solution = get_solution(400, 400)
print("The length of the solution is", len_of_solution)
# print(len(solution))

