from circleshape import CircleShape
from shot import Shot
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def turn(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        if self.cooldown <= 0:
            s = Shot(self.position)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
            self.cooldown = 0.3
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.turn(-1*dt)
        if keys[pygame.K_d]:
            self.turn(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.cooldown > 0:
            self.cooldown -= dt 
