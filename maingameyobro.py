import sys, pygame, random, pandas as pd
from ship import Ship
from asteroid import Asteroid
import matplotlib.pyplot as plot
import numpy as np
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()
background = pygame.image.load('background.png')
bg_rect = background.get_rect()

size = (width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_w * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#read and store game data
df = pd.read_csv('game_info.csv')
#df = datafile

#set up game variables
asteroids = pygame.sprite.Group()
numLevels = df['LevelNum'].max
level = df['LevelNum'].min()
levelData = df.iloc[level]
asteroidCount = levelData['AsteroidCount']
player = Ship((levelData['PlayerX'], levelData['PlayerY']))
tries = 0
totalTries = []

def init():
    global asteroidCount, asteroids, levelData, tries
    levelData = df.iloc[level]
    player.reset((levelData['PlayerX'], levelData['PlayerY']))
    asteroids.empty()
    asteroidCount = levelData['AsteroidCount']
    for i in range(asteroidCount):
        asteroids.add(Asteroid((random.randint(50, width - 50), random.randint(50, height -50)), random.randint(15, 60)))
    tries = 1

def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You won :D", True (0,0,0,))
    text_rect = text.get_rect()
    text_rect.center = width/2, height/2

    #create bar graph
    index = np.arange(len(totalTries))
    plot.bar(index, totalTries)
    plot.xlabel('Level Number', fontsize=15)
    plot.ylabel('Tries', fontsize=15)
    plot.xticks(index, totalTries, fontsize=20, rotation=5)
    plot.title('Tries per level:')
    plot.show()

    while True:
        screen.fill(color)
        screem.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit

def main():
    global level, tries, totalTries
    init()
    while level <= numLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player.speed[0] = 10
                if event.key == K_LEFT:
                    player.speed[0] = -10
                if event.key == K_UP:
                    player.speed[1] = 10
                if event.key == K_DOWN:
                    player.speed[1] = -10
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player.speed[0] = 0
                if event.key == K_LEFT:
                    player.speed[0] = 0
                if event.key == K_UP:
                    player.speed[1] = 0
                if event.key == K_DOWN:
                    player.speed[1] = 0
        screen.fill(color)
        screen.blit(background, bg_rect)
        player.update()
        asteroids.update()
        gets_hit = pygame.sprite.spritecollide(player, asteroids, False)
        asteroids.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()

        if player.checkReset(width):
            totalTries.append(tries)
            if level == numLevels:
                break
            else:
                level += 1
                init()
        elif gets_hit:
            player.reset((levelData['PlayerX'], levelData['PlayerY']))
            tries +=1
    win()

if __name__ == '__main__':
    main()