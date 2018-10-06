import pygame
from game_functions import text_e, text_p , snake, fruit
from random import randrange

pygame.init()

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

largura = 360
altura = 480
tamanho = 10

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

pos_x = randrange(0, largura - tamanho, 10)
pos_y = randrange(0, altura - tamanho, 10)
ma_x = randrange(0, largura - tamanho, 10)
ma_y = randrange(0, altura - tamanho, 10)

velocidade_x = 0
velocidade_y = 0
cobra_xy = []
tam_cobra = 1
placar = 0

game_over = False
continua = True

while continua:

    while game_over:

        fundo.fill(preto)
        text_e('Game over, tecle E para sair ou C para continuar', branco)
        text_p('Pontuação: {}'.format(placar), branco)
        pygame.display.update()

        for eventos in pygame.event.get():

            if eventos.type == pygame.QUIT:

                continua = False
                game_over = False

            if eventos.type == pygame.KEYDOWN:

                if eventos.key == pygame.K_e:

                    continua = False
                    game_over = False

                if eventos.key == pygame.K_c:

                    pos_x = randrange(0, largura - tamanho, 10)
                    pos_y = randrange(0, altura - tamanho, 10)
                    ma_x = randrange(0, largura - tamanho, 10)
                    ma_y = randrange(0, altura - tamanho, 10)

                    velocidade_x = 0
                    velocidade_y = 0
                    cobra_xy = []
                    tam_cobra = 1
                    placar = 0

                    game_over = False
                    continua = True

    if continua:

        fundo.fill(preto)
        cobra_inicio = []
        cobra_inicio.append(pos_x)
        cobra_inicio.append(pos_y)
        cobra_xy.append(cobra_inicio)
        snake(cobra_xy)

        if len(cobra_xy) == tam_cobra:

            del cobra_xy[0]

        if any(bloco == cobra_inicio for bloco in cobra_xy[:-1]):

            game_over = True

        if pos_x == ma_x and pos_y == ma_y:

            ma_x = randrange(0, largura - tamanho, 10)
            ma_y = randrange(0, altura - tamanho, 10)
            tam_cobra += 1
            placar += 1

        fruit(ma_x, ma_y)
        pos_x += velocidade_x
        pos_y += velocidade_y
        pygame.display.update()
        relogio.tick(7)

        # if pos_x >= largura:
        #     pos_x = 0
        #
        # if pos_x < 0:
        #     pos_x = largura - tamanho
        #
        # if pos_y >= altura:
        #     pos_y = 0
        #
        # if pos_y < 0:
        #     pos_y = altura - tamanho

        if pos_x > largura:

            game_over = True

        if pos_x < 0:

            game_over = True

        if pos_y > altura:

            game_over = True

        if pos_y < 0:

            game_over = True

    for eventos in pygame.event.get():

        if eventos.type == pygame.QUIT:

            continua = False

        if eventos.type == pygame.KEYDOWN:

            if eventos.key == pygame.K_LEFT and velocidade_x != tamanho:

                velocidade_y = 0
                velocidade_x = - tamanho

            if eventos.key == pygame.K_RIGHT and velocidade_x != -tamanho:

                velocidade_y = 0
                velocidade_x = tamanho

            if eventos.key == pygame.K_DOWN and velocidade_y != - tamanho:

                velocidade_x = 0
                velocidade_y = tamanho

            if eventos.key == pygame.K_UP and velocidade_y != tamanho:

                velocidade_x = 0
                velocidade_y = - tamanho

pygame.quit()
