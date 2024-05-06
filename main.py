#importando o pygame
import pygame as pg

x = 350
y = 443
pg.init() #inicializa os módulos básicos do pygame

#Criação e configuração da tela
tela = pg.display.set_mode((800, 500))

#localização carros
carro_1_posicao_x = 0
carro_2_posicao_x = 0
carro_3_posicao_x = 0

#nomeando a tela
pg.display.set_caption('Meu primeiro jogo')

#carregamento de imagens e objetos
estrada = pg.image.load("imagens/estrada.png")
personagem_mario = pg.image.load("imagens/mario.png")
carro_1 = pg.image.load("imagens/carro-1.png")
carro_2 = pg.image.load("imagens/carro-2.png")
carro_3 = pg.image.load("imagens/carro-3.png")

#rotacionando os carros
carro_1 = pg.transform.rotate(carro_1, 180)
carro_2 = pg.transform.rotate(carro_2, 180)
carro_3 = pg.transform.rotate(carro_3, 180)

#clock para regular o FPS
clock = pg.time.Clock()

#loop principal do jogo
rodando = True
while rodando: # A variavel "rodando" irá controlar o termino do jogo
    #tratamento de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT: # Evento que indica o clique no botão de fechar
            rodando = False
            
    keys = pg.key.get_pressed() 

    if keys[pg.K_UP]:
        y -= 5
    if keys[pg.K_DOWN]:
        y += 5
    if keys[pg.K_LEFT]:
        x -= 5
    if keys[pg.K_RIGHT]:
        x += 5



    #atualiza objetos
    estrada = pg.transform.scale(estrada,(800,500))
    personagem_mario = pg.transform.scale(personagem_mario,(80, 70))
    carro_1 = pg.transform.scale(carro_1, (60,50))
    carro_2 = pg.transform.scale(carro_2, (60,50))
    carro_3 = pg.transform.scale(carro_3, (60,50))
    
    #movendo carro 1
    carro_1_posicao_x += 5
    #se chegar na posição maxima da tela, volta a posição inicial
    if carro_1_posicao_x == 800:
        carro_1_posicao_x = 0

    #movendo carro 2
    carro_2_posicao_x += 10
    #se chegar na posição maxima da tela, volta a posição inicial
    if carro_2_posicao_x == 800:
        carro_2_posicao_x = 0

    #movendo carro 3
    carro_3_posicao_x += 6
    #se chegar na posição maxima da tela, volta a posição inicial
    if carro_3_posicao_x >= 800:
        carro_3_posicao_x = 0

    #desenha objeto
    tela.blit(estrada,(0,0))
    tela.blit(personagem_mario,(x,y))
    tela.blit(carro_1, (carro_1_posicao_x,50))
    tela.blit(carro_2, (carro_2_posicao_x,120))
    tela.blit(carro_3, (carro_3_posicao_x,190))
    

    pg.display.update()#atualiza a tela

    clock.tick(60)#regulagem do FPS