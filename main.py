import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameclock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # instantiate AsteroidField object
    starfield = AsteroidField()

    # instantiate Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    itme = Player(x, y)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
        screen.fill("black")

        for member in updatable:
             member.update(dt)

        for asteroid in asteroids:
            if asteroid.collisioncheck(itme) == True:
                 print("Game over!")
                 sys.exit()


        for member in drawable:
             member.draw(screen)

        pygame.display.flip()

        # limit the timeframe to 60 FPS
        dt = gameclock.tick(60) / 1000
        
   

if __name__ == "__main__":
    main()

