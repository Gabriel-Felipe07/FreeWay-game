import pygame 

class janelaPrincipal:
    def __init__(self, width, height):
        pygame.init()  # Inicializa o pygame
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        
    def estrada(self):
        estrada = pygame.image.load("imagens/estrada.png")
        estrada = pygame.transform.scale(estrada, (self.width, self.height))
        self.display.blit(estrada, (0,0))

class jogador:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def criaJogador(self, pos_x, pos_y, tela):
        mario = pygame.image.load("imagens/mario.png")
        mario = pygame.transform.scale(mario, (self.width, self.height))
        tela.blit(mario, (pos_x, pos_y))

# Criando janela    
janela = janelaPrincipal(800, 500)
janela.estrada()

# Criando personagem
personagem = jogador(80, 70)
personagem.criaJogador(350, 443, janela.display)

# Clock para regulagem de fps
clock = pygame.time.Clock()

# Loop principal
rodando = True
while rodando:  # A variável "rodando" irá controlar o término do jogo
    # Tratamento de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Evento que indica o clique no botão de fechar
            rodando = False
            
    # Atualizando janela
    pygame.display.update()

    # Definindo o fps
    clock.tick(60)

# Encerrando o pygame
pygame.quit()