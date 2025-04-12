from circleshape import CircleShape
import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        da = random.uniform(20, 50)
        vs1 = self.velocity.rotate(da) * 1.2
        vs2 = self.velocity.rotate(-da) * 1.2
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_a1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_a1.velocity = vs1
        new_a2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_a2.velocity = vs2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    