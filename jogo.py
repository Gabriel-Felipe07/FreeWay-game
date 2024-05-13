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
    def __init__(self, width, height, pista, velocidade, tipo):
        self.width = width
        self.height = height
        self.pista = pista  # Identificador da pista (1, 2, 3, etc.)
        self.velocidade = velocidade  # Velocidade horizontal dos carros
        self.pos_x = 0  # Começam da borda esquerda
        self.pos_y = self.pista
        self.tipo_carro = tipo

    def move_carro(self):
        # O carro vai andando conforme a velocidade descrita
        self.pos_x += self.velocidade
        # Se o carro passar do limite da tela, redefine sua posição para a posição inicial
        if self.pos_x > 800:
            self.pos_x = -self.width

    def cria_carros(self, tela):
        # Desenha o carro na tela com sua posição atualizada
        carro_img = pygame.image.load(self.tipo_carro)  # Ajuste para cada carro
        carro_img = pygame.transform.rotate(carro_img, 180)
        carro_img = pygame.transform.scale(carro_img, (self.width, self.height))
        tela.blit(carro_img, (self.pos_x, self.pos_y))

class Colisao:
    def verifica_colisao(objeto1, objeto2):
        # Verifica se há colisão entre dois retângulos
        if (objeto1.pos_x < objeto2.pos_x + objeto2.width and
            objeto1.pos_x + objeto1.width > objeto2.pos_x and
            objeto1.pos_y < objeto2.pos_y + objeto2.height and
            objeto1.pos_y + objeto1.height > objeto2.pos_y):
            return True
        else:
            return False

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

    # Verifica colisão entre o personagem e os carros
    for carro in carros:
        if Colisao.verifica_colisao(personagem, carro):
            # Ação a ser tomada quando houver colisão
            # Por exemplo, reiniciar a posição do personagem
            personagem.pos_x = 350
            personagem.pos_y = 443

    # Desenhar objetos
    janela.estrada()
    for carro in carros:
        carro.cria_carros(janela.display)

    personagem.movimentacao_jogador()
    personagem.cria_jogador(janela.display)

    # Atualizar janela
    pygame.display.update()
    clock.tick(60)