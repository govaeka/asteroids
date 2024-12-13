import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        vect1 = pygame.math.Vector2.rotate(self.velocity, angle)
        vect2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_pos_x = self.position.x
        new_pos_y = self.position.y
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(new_pos_x, new_pos_y, new_radius)
        ast2 = Asteroid(new_pos_x, new_pos_y, new_radius)
        ast1.velocity = vect1 * 1.2
        ast2.velocity = vect2 * 1.2



        