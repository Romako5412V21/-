import pygame
pygame.init()
import random
font = pygame.font.Font(None,24)
Tekst= font.render("Пук", True,(200,200,200))

score = 0
clock = pygame.time.Clock()
window = pygame.display.set_mode((1366,700))
back_color = (255, 198, 112)
game = True
players = [
pygame.Rect(350,250,100,200),
pygame.Rect(550,250,100,200),
pygame.Rect(750,250,100,200),
pygame.Rect(950,250,100,200)]
text_on_areo = random.choice(players)
start_time = pygame.time.get_ticks()
while game:
    
    window.fill(back_color)
    window.blit(Tekst,(380,350))
    
    for pl in players:
        pygame.draw.rect(window,(100,50,50),pl)

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    if elapsed_time > 1000:
        text_on_areo = random.choice(players)
        start_time = pygame.time.get_ticks()
    window.blit(Tekst,(text_on_areo.x+30,text_on_areo.y+100))


  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if text_on_areo.collidepoint(x,y):
                score += 1
                print(score)
        elif event.type == pygame.KEYDOWN:
            print('Пук')


    clock.tick(120)
    pygame.display.update()