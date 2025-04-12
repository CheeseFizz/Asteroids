import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set sprite groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    # Init sprites
    playerShape = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    afield = AsteroidField()


    # Game loop
    while True:
        # Handle events / update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        # Check collisions
        for a in asteroids:
            if playerShape.collision(a):
                print("Game over!")
                return
            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split()


        # Do screen stuff
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Do time management stuff
        dt = (clock.tick(60))/1000



if __name__ == "__main__":
    main()
