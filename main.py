
from asteroidfield import AsteroidField
import pygame
from constants import (SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_TURN_SPEED)
from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
import sys

def main():
    try:
        pygame.init()
        print("Pygame initialized successfully!")
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Display set successfully!")
        
        clock = pygame.time.Clock()
        
        dt = 0
        
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()  
        shots = pygame.sprite.Group()
        Player.containers = (updatable,drawable,shots)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        asteroid_field = AsteroidField()
       
        while True:
            dt = clock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            


            updatable.update(dt)
            player.update(dt)
            player.shots.update(dt) 


            screen.fill((0, 0, 0))
            
            

            

            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    print("Game over!")
                    sys.exit()
        


            for sprite in drawable:
                sprite.draw(screen)            
            player.shots.draw(screen)
            
            
            pygame.display.flip()
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

 























































