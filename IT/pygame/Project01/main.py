import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

ducImage = pygame.image.load('./IT/pygame/Project01/duc.png').convert_alpha()
ducImage = pygame.transform.scale(ducImage,
                                  (ducImage.get_width()*0.5,
                                   ducImage.get_height()*0.5,
                                   ))

running = True
x = 0

clock = pygame.time.Clock()
deltaTime = 0.1


while running:
    screen.fill((255, 255, 255))
    
    screen.blit(ducImage, (x, 30))
    
    x += 25 * deltaTime
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    pygame.display.flip()
    deltaTime = clock.tick(60)
    deltaTime = max(0.001, min(0.1, deltaTime))
    
    
pygame.quit()
print('\033[31m'+"Game Quited")