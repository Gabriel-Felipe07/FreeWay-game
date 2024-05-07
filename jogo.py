import pygame

class JanelaPrincipal:
    def __init__(self, width, height):
        pygame.init()  # Inicializa o pygame
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        
    def estrada(self):
        estrada = pygame.image.load("imagens/estrada.png")
        estrada = pygame.transform.scale(estrada, (self.width, self.height))
        self.display.blit(estrada, (0,0))

class Jogador:
    def __init__(self, width, height, pos_x, pos_y):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def cria_jogador(self, tela):
        mario = pygame.image.load("imagens/mario.png")
        mario = pygame.transform.scale(mario, (self.width, self.height))
        tela.blit(mario, (self.pos_x, self.pos_y))

    def movimentacao_jogador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.pos_y -= 5
        elif keys[pygame.K_DOWN]:
            self.pos_y += 5
        elif keys[pygame.K_LEFT]:
            self.pos_x -= 5
        elif keys[pygame.K_RIGHT]:
            self.pos_x += 5

        if self.pos_x >= 800 or self.pos_x <= 0:
            self.pos_x = 350
            self.pos_y = 443
        if self.pos_y >= 500 or self.pos_y <= 0:
            self.pos_y = 443
            self.pos_x = 350

# Criando janela    
janela = JanelaPrincipal(800, 500)
janela.estrada()

# Criando personagem
personagem = Jogador(80, 70, 350, 443)

# Clock para regulagem de fps
clock = pygame.time.Clock()

# Loop principal
rodando = True
while rodando:
    # Tratamento de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    # Movimentação do jogador
    personagem.movimentacao_jogador()

    # Desenhar objetos
    janela.estrada()
    personagem.cria_jogador(janela.display)

    # Atualizar janela
    pygame.display.update()

    # Definindo o fps
    clock.tick(60)

pygame.quit()
