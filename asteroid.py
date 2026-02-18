from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random





class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        color = "white"
        pos = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, pos, radius, LINE_WIDTH)  

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        rand_degree = random.uniform(20.0, 50.0)
        vector1 = self.velocity.rotate(rand_degree)
        vector2 = self.velocity.rotate(-rand_degree)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid( self.position.x, self.position.y, smaller_radius)
        asteroid.velocity = vector1 * 1.2
        asteroid = Asteroid( self.position.x, self.position.y, smaller_radius)
        asteroid.velocity = vector2 * 1.2