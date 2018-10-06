import pygame

pygame.font.init()

largura = 360
altura = 480
tamanho = 10

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

fundo = pygame.display.set_mode((largura, altura))
font = pygame.font.SysFont(None, 18)


def text_e(msg, cor):

    texto = font.render(msg, True, cor)
    fundo.blit(texto, [largura/10, altura/5])

def text_p(msg, cor):

    texto = font.render(msg, True, cor)
    fundo.blit(texto, [largura/3, altura/3])

def snake(cobra_xy):

    for xy in cobra_xy:
        pygame.draw.rect(fundo, verde, [xy[0], xy[1], tamanho, tamanho])

def fruit(pos_x, pos_y):

    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])
