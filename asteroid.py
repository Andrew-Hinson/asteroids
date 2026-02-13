from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, radius)


    def draw(self, screen):
        color = "white"
        pos = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, pos, radius, LINE_WIDTH)  

    def update(self, dt):
        self.position += self.velocity * dt
