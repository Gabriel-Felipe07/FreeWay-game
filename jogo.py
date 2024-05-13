import random
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
    def __init__(self, width, height, pos_x, pos_y, imagem):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))

        self.mascara = pygame.mask.from_surface(self.imagem)

    def cria_jogador(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

    def movimentacao_jogador(self, velocidade):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.pos_y -= velocidade
        elif keys[pygame.K_DOWN]:
            self.pos_y += velocidade
        elif keys[pygame.K_LEFT]:
            self.pos_x -= velocidade
        elif keys[pygame.K_RIGHT]:
            self.pos_x += velocidade

        if self.pos_x >= 800 or self.pos_x <= 0:
            self.pos_x = 350
            self.pos_y = 443
        if self.pos_y >= 500 or self.pos_y <= 0:
            self.pos_y = 443
            self.pos_x = 350

class Carros:
    def __init__(self, width, height, pista, velocidade, tipo):
        self.width = width
        self.height = height
        self.pista = pista  # Identificador da pista (1, 2, 3, etc.)
        self.velocidade = velocidade  # Velocidade horizontal dos carros
        self.pos_x = 0  # Começam da borda esquerda
        self.pos_y = self.pista
        self.imagem = pygame.image.load(tipo)
        self.imagem = pygame.transform.rotate(self.imagem, 180)
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))

        self.mascara = pygame.mask.from_surface(self.imagem)


    def move_carro(self):
        # O carro vai andando conforme a velocidade descrita
        self.pos_x += self.velocidade
        # Se o carro passar do limite da tela, redefine sua posição para a posição inicial
        if self.pos_x > 800:
            self.pos_x = -self.width

    def cria_carros(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

# Criando carros
carros = [Carros(100, 50, 40, random.randint(3,15), "imagens/carro-1.png"),  # Carro na pista 1
          Carros(120, 60, 110, random.randint(5,15), "imagens/carro-2.png"),  # Carro na pista 2
          Carros(110, 55, 180, random.randint(9,15), "imagens/carro-3.png"),  # Carro na pista 3
          Carros(110, 55, 250, random.randint(5,15), "imagens/carro-1.png"), # Carro na pista 4
          Carros(110, 55, 320, random.randint(10,20), "imagens/carro-2.png"), # Carro na pista 5
          Carros(110, 55, 390, random.randint(5,15), "imagens/carro-3.png")] # Carro na pista 6

# Criando janela    
janela = JanelaPrincipal(800, 500)
janela.estrada()

# Criando personagem
personagem = Jogador(80, 70, 350, 443, "imagens/mario.png")

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

    personagem.movimentacao_jogador(6)
    personagem.cria_jogador(janela.display)

    for carro in carros:
        if personagem.mascara.overlap(carro.mascara,(carro.pos_x - personagem.pos_x, carro.pos_y - personagem.pos_y)):
            personagem.pos_x = 350
            personagem.pos_y = 443

    # Atualizar janela
    pygame.display.update()
    clock.tick(60)