import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot


def main():
    pygame.init()
    pygame.font.init()
    FONT = pygame.font.SysFont("Arial", 24)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(x, y)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    while True:
        score_board = FONT.render(f"Score: {score}", True, "white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        log_state()
        updatable.update(dt)
        screen.fill("black")
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("You were hit by an asteroid! Game Over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += 1
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        screen.blit(score_board, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()