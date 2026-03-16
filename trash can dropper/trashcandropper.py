import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
x = 100
y = 100
adding = random.randint(1, 4)
vx = 5
vx2 = 0
moving = True
clock = pygame.time.Clock()
running = True
trash = pygame.image.load("trash.png")
can = pygame.image.load("can.png")
counter = 0
font = pygame.font.Font(None, size=60)
while running:
     
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if moving:
                    moving = not moving
    
    if moving:
        x += vx
    
    if not moving:
        y += 8
    
    
    if x >= 1280:
            vx = -vx
            
    if x <= 0:
            vx = -vx
    
    hitboxcan = can.get_rect(topleft=(570,490))
    hitboxtrash = trash.get_rect(topleft=(x,y))
    
    if hitboxtrash.colliderect(hitboxcan):
        x = 100
        y = 100
        moving = True
        vx = (abs(vx) + adding)
        counter += 1
    
    if y >= 720:
        x = 100
        y = 100
        moving = True
        
    adding = random.randint(1, 7)
    
    text = font.render(str(counter), True, (255, 255, 255))
    
    screen.fill((0,0,0))
    screen.blit(text, (610, 20))
    screen.blit(trash, (x,y))
    screen.blit(can, (570, 490))
    clock.tick(60)
    
    pygame.display.flip()
    
pygame.quit()