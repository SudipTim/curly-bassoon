import pygame

pygame.init()

screen_Width=1366
screen_height=720
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((screen_Width,screen_height))

player = pygame.Rect((300,250,50,50))

run=True
while run:

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,50,100), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1,0)              
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()            

