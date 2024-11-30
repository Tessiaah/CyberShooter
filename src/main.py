import pygame
import sys
import random
from Enemies import Enemy

# function definitions

# refactor this later
def createenemies(spawnpoints: list[tuple], enemylist: list[Enemy], enemieslalive: list[Enemy]):
    while True:
        index = random.randint(0, 2)
        enemy = random.choice(enemylist)
        if isenemyvalid(enemy, enemieslalive) and ispostionvalid(spawnpoints[index], enemieslalive):
            enemy.position = spawnpoints[index]
            enemieslalive.append(enemy)
            break


def ispostionvalid(position, enemiesalive: list[Enemy]):
    for enemies in enemiesalive:
        if position == enemies.position:
            return False
    return True


def isenemyvalid(enemy, enemiesalive):
    if enemy in enemiesalive:
        return False
    return True


def killclick(mouse, enemy, enemiesalive: list[Enemy]):
    enemy_rect = pygame.Rect(enemy.position[0], enemy.position[1], enemy.sprite.get_width(), enemy.sprite.get_height())
    if enemy_rect.collidepoint(mouse):
        enemy.takedamage(playerDamage)

        # print(f"{enemy.hp}")
        if enemy.isdead():
            enemiesalive.remove(enemy)
            enemy.fullheal()


# list of possible enemy spawnpoints
spawnPoints = [(800, 400), (1300, 200), (200, 100)]


# enemy image setup
lightEnemySprite = pygame.image.load("../assets/lightenemy.png")
heavyEnemySprite = pygame.image.load("../assets/heavyenemy.png")
fastEnemySprite = pygame.image.load("../assets/fastenemy.png")

# enemy creation
heavyEnemy = Enemy(3,3, heavyEnemySprite, )
lightEnemy = Enemy(1,1, lightEnemySprite)
fastEnemy = Enemy(2,2, fastEnemySprite)
enemyList = [heavyEnemy, lightEnemy, fastEnemy]

# player setup
playerDamage = 1
crosshair = pygame.image.load("../assets/crosshair.png")
crosshair_width, crosshair_height = crosshair.get_size()

# initializations
pygame.init()
pygame.mixer.init()



# sfx setup

pygame.mixer.music.load("../assets/bgm.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

shoot_sound = pygame.mixer.Sound("../assets/gunshot.mp3")

pygame.mouse.set_visible(False)

enemiesAlive = []

width, height = 1600, 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CyberShooter")

background_image = pygame.image.load("../assets/back.png")


# mainloop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shoot_sound.play()
            mouse_pos = pygame.mouse.get_pos()
            for e in enemiesAlive:
                killclick(mouse_pos, e, enemiesAlive)

    screen.blit(pygame.transform.scale(background_image, (width, height)), (0, 0))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    crosshairpos = (mouse_x - crosshair_width // 2, mouse_y - crosshair_height // 2)

# ensures that there are always 2 enemies in the screen
    if len(enemiesAlive) < 2:
        createenemies(spawnPoints, enemyList, enemiesAlive)

    #screen.blit(pygame.transform.scale(background_image, (width, height)), (0, 0))

    for enemy in enemiesAlive:
        screen.blit(enemy.sprite, (enemy.position[0], enemy.position[1]))

    screen.blit(crosshair, crosshairpos)

# Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()






