import pygame
import random
import time
pygame.init()
pygame.display.set_caption("Jogo do Meteoro")
tamanho = (600, 600)
display = pygame.display.set_mode(tamanho)
branco = (255, 255, 255)
preto = (0, 0, 0)
clock = pygame.time.Clock()
running = True
posicaoX = 300
movimentoX = 0
movimentoY = 0
posicaoY = 550
nave = pygame.image.load("foguetecerto.png")
fundo = pygame.image.load("imagemdefundo.jpg")
meteoro = pygame.image.load("meteoro.png")
meteoroSound = pygame.mixer.Sound("meteoro.mp3")
pygame.display.set_icon(meteoro)
posicaoXMeteoro = 300
posicaoYMeteoro = -100
velocidadeMeteoro = 1
direcaobolinha = True
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pontos = 0
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 50)
dificuldade = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movimentoX = - 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movimentoX = + 5

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            movimentoY = - 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            movimentoY = + 5

        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            movimentoY = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            movimentoY = 0

        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movimentoX = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movimentoX = 0
    if posicaoX > 500:
        posicaoX = 500
    elif posicaoX < 0:
        posicaoX = 0
    if posicaoY > 500:
        posicaoY = 500

    elif posicaoY < 0:
        posicaoY = 0
    else:
        posicaoX = posicaoX + movimentoX
        posicaoY = posicaoY + movimentoY

    display.blit(fundo, (0, 0))
    # pygame.draw.circle(display, branco, (posicaoX, posicaoY), 30)
    display.blit(nave, (posicaoX, posicaoY))

    if posicaoYMeteoro > 600:
        posicaoYMeteoro = -100
        posicaoXMeteoro = random.randint(0, 600)
        velocidadeMeteoro = velocidadeMeteoro + 1
        pontos = pontos + 1
        pygame.mixer.Sound.play(meteoroSound)

    posicaoYMeteoro = posicaoYMeteoro + velocidadeMeteoro

    # display.blit(missil, (300, 0))
    display.blit(meteoro, (posicaoXMeteoro, posicaoYMeteoro))
    texto = font.render("Pontos: "+str(pontos), True, (255, 255, 255))
    display.blit(texto, (10, 10))
    clock.tick(60)

    pixelsYNave = list(range(posicaoY, posicaoY + 100))
    pixelsXNave = list(range(posicaoX, posicaoX + 100))

    # 101 é o tamanho da imagem
    pixelsYMeteoro = list(range(posicaoYMeteoro, posicaoYMeteoro+100))
    pixelsXMeteoro = list(range(posicaoXMeteoro, posicaoXMeteoro+100))

    if len(list(set(pixelsXNave) & set(pixelsXMeteoro))) > dificuldade:
        if len(list(set(pixelsYNave) & set(pixelsYMeteoro))) > dificuldade:
            youlose = "YOU LOSE"
            texto2 = font2.render(youlose, True, (255, 255, 255))
            display.blit(texto2, (230, 300))

            running = False
            print("Morreu!")

    pygame.display.update()
time.sleep(3)
pygame.quit()
