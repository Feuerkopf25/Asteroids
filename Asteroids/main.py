import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    print("Starting Asteroids")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    Asteroid_field = AsteroidField()

    player = Player(x, y)

    dt = 0

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_for_collision(shot):
                    asteroid.kill()
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
