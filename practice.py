import pygame

pygame.init()

screen_Width=1366
screen_height=720
x=700
y=550
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((screen_Width,screen_height))

player = pygame.Rect((300,250,50,50))
img=pygame.image.load("bear.png")
pygame.display.set_icon(img)
player=pygame.image.load("rocket.png")
vel=2
def players():
        screen.blit(player,(x,y))

run=True
while run:
    pygame.time.delay(3)
    screen.fill((10,10,10))
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1,0)              
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    if key[pygame.K_w] == True and y > 0 :
        y-=vel
    elif key[pygame.K_s] == True and y < 650 :
        y+=vel

    elif key[pygame.K_a] == True and x > 0 :
        x-=vel       
           
    elif key[pygame.K_d] == True and x < 1300 :
        x+=vel   
        print(x)     
           
    players()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()            

