import pygame
import time
import random

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
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += random.randint(-20, 20)
        monster_y += random.randint(-20,20)
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
        screen.blit(hero_image, (224, 208))
        screen.blit(monster_image, (monster_x, monster_y))
        pygame.display.update()
        clock.tick(60)
        time.sleep(2)

    pygame.quit()

if __name__ == '__main__':
    main()
