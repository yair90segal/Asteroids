import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt_undevided = clock.tick(60)
        dt = dt_undevided / 1000



if __name__ == "__main__":
    main()

