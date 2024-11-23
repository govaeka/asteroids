import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameclock = pygame.time.Clock()
    dt = 0

    # instantiate player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    itme = Player(x, y)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
        screen.fill("black")

        itme.update(dt)

        itme.draw(screen)

        pygame.display.flip()

        # limit the timeframe to 60 FPS
        dt = gameclock.tick(60) / 1000
        
   

if __name__ == "__main__":
    main()

