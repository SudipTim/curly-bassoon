import pygame
import random
pygame.init()

screen_Width=1366
screen_height=720

player_x=700
player_y=550

bullet_x=player_x+15
bullet_y=player_y+60

enemy_x=1300
enemy_y=0

pygame.display.set_caption("Game")
screen = pygame.display.set_mode((screen_Width,screen_height))
img=pygame.image.load("bear.png")
pygame.display.set_icon(img)


player=pygame.image.load("rocket.png")
enemy=pygame.image.load("alien.png")
bg=pygame.image.load("spacebg2.jpg")
bullet=pygame.image.load("bullett.png")

bullet_vel=10
vel=2.5
enemy_xmovement = 2
enemy_ymovement = 40

moving_left= True
bullet_fired=False

def players():
        screen.blit(player,(player_x,player_y))

def enemies():
     screen.blit(enemy,(enemy_x,enemy_y))        

def bullet_func():
    global bullet_x, bullet_y, bullet_fired
    if bullet_fired:
        screen.blit(bullet,(bullet_x,bullet_y))
        bullet_y-=bullet_vel

        if bullet_y < 0 :
            bullet_fired= False


def bullet_reset():
    global bullet_x, bullet_y
    bullet_x = player_x+15
    bullet_y = player_y+20

run=True
while run:
    # pygame.time.delay()
    screen.fill((0,0,0))

    screen.blit(bg,(0,0))


    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True and player_y > 450 :
        player_y-=vel

    elif key[pygame.K_s] == True and player_y < 650 :
        player_y+=vel

    elif key[pygame.K_a] == True and player_x > 0 :
        player_x-=vel  
           
    elif key[pygame.K_d] == True and player_x < 1300 :
        player_x+=vel   



    if moving_left:
        enemy_x -= enemy_xmovement  # Move left
        if enemy_x <= 0:
            moving_left = False
            enemy_y+=enemy_ymovement # Change direction to right
    else:
        enemy_x += enemy_xmovement # Move right
        if enemy_x >= 1300:
            enemy_y+=enemy_ymovement
            moving_left = True 
             # Change direction to left

    if key[pygame.K_SPACE] == True and not bullet_fired:
        bullet_reset()
        bullet_fired = True
        

    
    enemies()       
    players()
    bullet_func()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()            

