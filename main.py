import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        for a in asteroids:
            if a.check_collision(p):
                print("Game Over!")
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        dt_undevided = clock.tick(60)
        dt = dt_undevided / 1000



if __name__ == "__main__":
    main()

