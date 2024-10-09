import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #player object
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    #asteroid objects
    Asteroid.containers = (updatable, drawable, asteroids)

    #asteroid field
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #shot objects
    Shot.containers = (shots, updatable, drawable)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print('Game Over!')
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()             
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit the framerate to 60 fps
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()