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
    enemy_xmovement.append(random.randint(1, 3))
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

font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10  # Set this to a suitable value within the screen bounds

gameover_font = pygame.font.Font("freesansbold.ttf", 42)
gtext_x = 550
gtext_y = 300  # Centered within the screen

game_over = False  # Flag to check if the game is over

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

def player_enemy_collision(player_x, player_y, enemy_x, enemy_y):
    # Check if the player and enemy overlap
    distance = math.sqrt(math.pow(player_x - enemy_x, 2) + (math.pow(player_y - enemy_y, 2)))
    return distance < 40  # Adjust this threshold as necessary

def show_score():
    global score  # Make sure to use the global score variable
    score_display = font.render("Score: " + str(score), True, (155, 155, 155))
    screen.blit(score_display, (text_x, text_y))
    
def gameover():
    gameover_text = gameover_font.render("Game Over!", True, (255, 0, 0))  # Red color for visibility
    restart_text = font.render("Press R to Restart or Q to Quit", True, (155, 155, 155))
    screen.blit(gameover_text, (gtext_x, gtext_y))
    screen.blit(restart_text, (gtext_x - 50, gtext_y + 50))  # Adjusted position for restart text

# Main game loop
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Player movement controls
    key = pygame.key.get_pressed()
    if not game_over:  # Only allow player movement if the game is not over
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
        if enemy_y[i] > 600:  # Check if any enemy has crossed the threshold
            game_over = True
            break

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
            enemy_y[i] = random.randint(0, 400)  # Ensure enemies are within the screen height

        # Check for player collision
        if player_enemy_collision(player_x, player_y, enemy_x[i], enemy_y[i]):
            game_over = True

        # Draw the enemy on the screen
        enemies(i)

    if not game_over:  # Draw player and bullet only if the game is not over
        players()  # Draw the player
        bullet_func()  # Draw the bullet
        show_score()  # Show the score
    else:
        gameover()  # Show game over message

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:  # Restart game
                    # Reset game state
                    player_x = 700
                    player_y = 550
                    bullet_fired = False
                    score = 0
                    game_over = False
                    # Reset enemy positions
                    for i in range(number_of_enemies):
                        enemy_x[i] = random.randint(0, 1000)
                        enemy_y[i] = random.randint(0, 400)

    pygame.display.update()
