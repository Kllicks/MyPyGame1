import pygame
import time
import random

# class Character:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.speed_x = 5
#         self.speed_y = 5
#         self.size = 32

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.randint(-1, 1)
        self.speed_y = random.randint(-1, 1)
        self.radius = 36
        self.image = pygame.image.load('images/hero.png').convert_alpha()
        
    
    def update(self, width, height):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x + self.radius > (width - self.radius):
            self.speed_x = random.randint(-1 , 0)
        if self.y + self.radius > (height - self.radius):
            self.speed_y = random.randint(-1 , 0)
        if self.x - self.radius < 0:
            self.speed_x = random.randint(0 , 1)
        if self.y - self.radius < 0:
            self.speed_y = random.randint(0 , 1)

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    hero = Hero(224, 208)
    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    hero.image 
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    monster_x = 36
    monster_y = 36
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += random.randint(-20, 20)
        monster_y += random.randint(-20,20)
        hero.update(width, height)
        if monster_x > width:
            monster_x = 0
        if monster_x < 0:
            monster_x = width
        if monster_y > height:
            monster_y = 0
        if monster_y < 0:
            monster_y = height

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero.image, (hero.x, hero.y))
        screen.blit(monster_image, (monster_x, monster_y))
        pygame.display.update()
        clock.tick(60)
        # time.sleep(2)

    pygame.quit()

if __name__ == '__main__':
    main()
