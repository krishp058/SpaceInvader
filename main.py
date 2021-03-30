import pygame
import random

# Intialize the pygame (Without this pygame can't work)
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Images/Spaceship_background_800x600.jpg")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Images/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('Images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Enemy
enemyImg = pygame.image.load('Images/alien.png')
enemyX = random.randint(0, 736)
# Makes the enemy spawn randomly - First parameter is starting value and second is ending
# Remember to import 'random'
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop (so the game can stay on and not end straight after it starts)
running = True
while running:

    # RGB - Red, Green, Blue - Changing background colour
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    # A event is anything that happens in the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Adds player control
    playerX += playerX_change

    # Adds player boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Adds enemy control
    enemyX += enemyX_change

    # Adds enemy movement
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Adds Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Adding player image & enemy
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Everything about the loop should be before this line because this updates the game screen/window
    pygame.display.update()
