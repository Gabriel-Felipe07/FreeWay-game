import pygame 

class janelaPrincipal:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
    def estrada(self):
        estrada = pygame.image.load("imagens/estrada.png")
        self.display.blit(estrada, (0,0))
    
janelaPrincipal(800, 500)

#clock para regulagem de fps
clock = pygame.time.Clock()

#loop principal
rodando = True
while rodando:# A variavel "RODANDO" irá controlar o termino do jogo
    #tratamento de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:#evento que indica o clique no botão de fechar
            rodando = False
        
    #atualizando janela
    pygame.display.update()

    #definindo o fps
    clock.tick(60)