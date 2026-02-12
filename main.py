import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()    
    date_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
   
    Player.containers = (updatable, drawable)

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(date_time)
        for drawitem in drawable:
            drawitem.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)
        date_time = delta_time / 1000

        
if __name__ == "__main__":
    main()
