import random
import pygame


class Platforms:
    def __init__(self, win_height, win_width, number_platforms):
        self.height = 5
        self.width = []
        self.number_platforms = number_platforms
        self.win_height = win_height
        self.win_width = win_width
        self.seed = 2

    def set_platform_position(self, i):
        width = random.randint(40, 150)
        x = random.randint(0, self.win_width - width)
        y = random.randint(self.win_height - 230 - (130*i), (self.win_height - 100 - (130*i)))
        return x, y, width

    def draw_platform(self, x, y, width, win):
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, self.height))

    def draw_center_platform(self, win, x, y):
        pygame.draw.rect(win, (0, 255, 0), (x, y, 5, 5))

    def set_platforms(self, win):
        platforms_coordinates = []
        for i in range(self.number_platforms):
            random.seed(self.seed + i)
            x, y, width = self.set_platform_position(i)
            self.width.append(width)
            platforms_coordinates.append((x, x + self.width[i], y))
            self.draw_platform(x, y, self.width[i], win)
            self.draw_center_platform(win, x, y)
            self.draw_center_platform(win, x + self.width[i], y)

        return platforms_coordinates

    def move_platforms(self, platforms_coordinates, win):
        for i, (x1, x2, y) in enumerate(platforms_coordinates):
            pygame.draw.rect(win, (255, 0, 0), (x1, y, self.width[i], self.height))