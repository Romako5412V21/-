import pygame
pygame.init()
import random
font = pygame.font.Font(None,24)
Tekst= font.render("RGB", True,(200,200,200))

clock = pygame.time.Clock()
window = pygame.display.set_mode((1366,700))
back_color = (255, 198, 112)
game = True


player = pygame.Rect(350,250,100,200)
player1 = pygame.Rect(550,250,100,200)
player2 = pygame.Rect(750,250,100,200)
player3 = pygame.Rect(950,250,100,200)

while game:

     
    window.fill(back_color)
     
    
    window.blit(Tekst,(50,50))

    pygame.draw.rect(window,(103, 239, 112) ,player)
    pygame.draw.rect(window,(103, 239, 112) ,player1)
    pygame.draw.rect(window,(103, 239, 112) ,player2)
    pygame.draw.rect(window,(103, 239, 112) ,player3)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(10)
        elif event.type == pygame.KEYDOWN:
            print("1")



    clock.tick(120)
    pygame.display.update()