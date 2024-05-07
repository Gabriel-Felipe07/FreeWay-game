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

class Carros:
    def __init__(self, width, height, pista, velocidade):
        self.width = width
        self.height = height
        self.pista = pista  # Identificador da pista (1, 2, 3, etc.)
        self.velocidade = velocidade  # Velocidade horizontal dos carros
        self.pos_x = 0  # Começam da borda esquerda
        self.pos_y = self.pista

    def move_carro(self):
        # Atualiza a posição horizontal do carro com base na velocidade
        self.pos_x += self.velocidade

        # Se o carro passar do limite da tela, redefine sua posição para a borda esquerda
        if self.pos_x > 800:
            self.pos_x = -self.width

    def cria_carros(self, tela):
        # Desenha o carro na tela com sua posição atualizada
        carro_img = pygame.image.load("imagens/carro-1.png")  # Ajuste para cada carro
        carro_img = pygame.transform.rotate(carro_img, 180)
        carro_img = pygame.transform.scale(carro_img, (self.width, self.height))
        tela.blit(carro_img, (self.pos_x, self.pos_y))

# Criando carros
carros = [Carros(100, 50, 50, 2),  # Carro na pista 1
          Carros(120, 60, 120, 3),  # Carro na pista 2
          Carros(110, 55, 190, 4)]  # Carro na pista 3

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
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação dos carros
    for carro in carros:
        carro.move_carro()

    # Desenhar objetos
    janela.estrada()
    for carro in carros:
        carro.cria_carros(janela.display)

    # Atualizar janela
    pygame.display.update()
    clock.tick(60)