import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_Width = 1366
screen_height = 720

# Set up the game window
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((screen_Width, screen_height))
img = pygame.image.load("bear.png")
pygame.display.set_icon(img)

# Player position
player_x = 700
player_y = 550

# Bullet initial position
bullet_x = player_x + 15
bullet_y = player_y + 60

# Enemy properties
enemy_x = []
enemy_y = []
enemy = []
enemy_xmovement = []
enemy_ymovement = []
enemy_directions = []  # List to store enemy movement directions
number_of_enemies = 4

for i in range(number_of_enemies):
    enemy_xmovement.append(random.randint(1,3))
    enemy_ymovement.append(40)
    enemy_x.append(random.randint(0, 1000))
    enemy_y.append(random.randint(0, 400))
    enemy.append(pygame.image.load("enemy.png"))
    enemy_directions.append(True)  # True for moving left, False for moving right

# Load images
player = pygame.image.load("rocket.png")
bg = pygame.image.load("spacebg2.jpg")
bullet = pygame.image.load("bullett.png")

# Bullet and player speed
bullet_vel = 10
vel = 2.5

bullet_fired = False
score = 0

# Functions to draw player, enemies, and bullet
def players():
    screen.blit(player, (player_x, player_y))

def enemies(i):
    screen.blit(enemy[i], (enemy_x[i], enemy_y[i]))

def bullet_func():
    global bullet_x, bullet_y, bullet_fired
    if bullet_fired:
        screen.blit(bullet, (bullet_x, bullet_y))
        bullet_y -= bullet_vel

        if bullet_y < 0:
            bullet_fired = False

def bullet_reset():
    global bullet_x, bullet_y
    bullet_x = player_x + 15
    bullet_y = player_y + 20

def bullet_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27  # Return True if collision occurs

# Main game loop
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Player movement controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player_y > 450:
        player_y -= vel
    if key[pygame.K_s] and player_y < 650:
        player_y += vel
    if key[pygame.K_a] and player_x > 0:
        player_x -= vel
    if key[pygame.K_d] and player_x < 1300:
        player_x += vel

    # Bullet firing
    if key[pygame.K_SPACE] and not bullet_fired:
        bullet_reset()
        bullet_fired = True

    # Update enemy positions and check for collisions
    for i in range(number_of_enemies):
        if enemy_directions[i]:  # Moving left
            enemy_x[i] -= enemy_xmovement[i]
            if enemy_x[i] <= 0:
                enemy_directions[i] = False  # Change direction to right
                enemy_y[i] += enemy_ymovement[i]  # Move down
        else:  # Moving right
            enemy_x[i] += enemy_xmovement[i]
            if enemy_x[i] >= screen_Width:
                enemy_directions[i] = True  # Change direction to left
                enemy_y[i] += enemy_ymovement[i]  # Move down

        # Check for bullet collision
        collision = bullet_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            score += 1
            print(score)
            enemy_x[i] = random.randint(0, 1000)
            enemy_y[i] = random.randint(0, 00)  # Ensure enemies are within the screen height

        # Draw the enemy on the screen
        enemies(i)

    players()  # Draw the player
    bullet_func()  # Draw the bullet

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
