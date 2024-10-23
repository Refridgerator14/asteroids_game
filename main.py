

import pygame
from constants import (SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_TURN_SPEED)
from player import Player

def main():
    try:
        pygame.init()
        print("Pygame initialized successfully!")
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Display set successfully!")
        
        clock = pygame.time.Clock()
        
        dt = 0
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        Player.containers = (updatables,drawables)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            for thing in updatables:
                thing.update()
                return thing
            for stuff in drawables:
                stuff.update()
                return stuff


            dt = clock.tick(60) / 1000
            screen.fill((0, 0, 0))
           
            player.update(dt)

            player.draw(screen)
           
            pygame.display.flip()
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

 























































