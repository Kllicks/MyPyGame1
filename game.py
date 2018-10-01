import pygame
import time
import random

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.size = 32

class Hero(Character):
    def __init__(self, x, y):
        self.x = 1
        self.y = 1

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    monster_x = 36
    monster_y = 36
    hero_x = 224
    hero_y = 208
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += random.randint(-20, 20)
        monster_y += random.randint(-20,20)
        hero_x += random.randint(-50, 50)
        hero_y += random.randint(-50, 50)
        if monster_x > width:
            monster_x = 0
        if monster_x < 0:
            monster_x = width
        if monster_y > height:
            monster_y = 0
        if monster_y < 0:
            monster_y = height
        if hero_x > (width - 36):
            hero_x = (width - 36)
        if hero_x < 36:
            hero_x = 36
        if hero_y > (height - 36):
            hero_y = (height - 36)
        if hero_y < 36:
            hero_y = 36
        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (hero_x, hero_y))
        screen.blit(monster_image, (monster_x, monster_y))
        pygame.display.update()
        clock.tick(60)
        # time.sleep(2)

    pygame.quit()

if __name__ == '__main__':
    main()
