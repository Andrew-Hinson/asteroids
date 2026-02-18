import pygame
import sys
from asteroid import Asteroid
from logger import log_state, log_event
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
from asteroidfield import AsteroidField




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()    
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable) 
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    AsteroidField.containers = updatable

    field = AsteroidField()

   



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()


        for drawitem in drawable:
            drawitem.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)
        dt = delta_time / 1000

        
if __name__ == "__main__":
    main()
