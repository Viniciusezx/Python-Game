import pygame
import random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Grid pra centralizar e definir a posição da maçã
def grid_maca():
    x = random.randint(0,500)
    y = random.randint(30,500)
    return (x//10 * 10, y//10 * 10)

# Colisão da cobra com a maçã
def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Reinicia as denições do jogo
def reiniciar_jogo():
    global pontos, cobra, maca_pos,my_direction, morreu
    pontos = 0
    cobra = [(100, 100), (110,100), (120,100), (130,100)]  # Corpo da cobra
    maca_pos = grid_maca()
    my_direction = LEFT
    morreu = False

# Definições da tela
pygame.init()
tela = pygame.display.set_mode((510, 540))
pygame.display.set_caption('Python Game')

# Pontos do jogador
pontos = 0
fonte_pontos = pygame.font.SysFont('arial', 25, True, False)

# Aparência/posição inicial da cobra
cobra = [(100, 100), (110,100), (120,100), (130,100)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((0,0,255))

# Aparência/posição inicial da maçã
maca = pygame.Surface((10,10))
maca.fill((255,0,0))
maca_pos = grid_maca()


muro = [(-8,2), (32,2), (72,2), (112,2), (358,2), (398,2), (438,2), (478,2),
        
        (-25,12), (15,12), (55,12), (95,12), (135,12), (335,12), (375,12), (415,12), (455,12), (495,12),
        
        (-8,22), (32,22), (72,22), (112,22), (152,22), (312,22), (352,22), (392,22), (432,22), (472,22)]

muro_skin = pygame.Surface((38,8))
muro_skin.fill((0,0,255))

muro_cima = (152,2),(335,2)
muro_cima_skin = pygame.Surface((21,8))
muro_cima_skin.fill((0,0,255))

muro_meio = (192,26), (232,26), (272,26)
muro_meio_skin = pygame.Surface((38,4))
muro_meio_skin.fill((0,0,255))

# Direção inicial da cobra
my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(7 + pontos)
    mensagem = f'PONTOS: {pontos}'
    texto_formatado = fonte_pontos.render(mensagem, False, (225,225,225))
    
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit() 
        
        if event.type == KEYDOWN:
            if event.key == K_w:
                my_direction = UP
            if event.key == K_s:
                my_direction = DOWN
            if event.key == K_d:
                my_direction = RIGHT
            if event.key == K_a:
                my_direction = LEFT

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    if colisao(cobra[0],maca_pos):
        maca_pos = grid_maca()
        cobra.append((0,0))
        pontos = pontos + 1

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    if cobra[0][0] < 0 or cobra[0][0] >= 510 or cobra[0][1] < 30 or cobra[0][1] >= 540:
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

    if cobra[0] in cobra[1:]:
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        

    tela.fill((0,0,0))
    
    for pos in muro:
        tela.blit(muro_skin, pos)
        
    for pos in muro_cima:
        tela.blit(muro_cima_skin, pos)
        
    for pos in muro_meio:
        tela.blit(muro_meio_skin, pos)
    
    tela.blit(texto_formatado, (187, -3))
    tela.blit(maca, maca_pos)
        
    for pos in cobra:
        tela.blit(cobra_skin, pos)

    pygame.display.update()
