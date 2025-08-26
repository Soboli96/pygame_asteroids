import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    background_color = (0, 0, 0)
    dt = 0

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updateable_group, drawable_group, asteroids)
    AsteroidField.containers = (updateable_group)
    asteroidfield = AsteroidField()

    Shot.containers = (updateable_group, drawable_group, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(background_color)

        updateable_group.update(dt)
        for sprite in drawable_group:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                raise SystemExit
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
