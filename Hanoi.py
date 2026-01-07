import pygame
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
POLE_HEIGHT = 100
POLE_WIDTH = 6
PLATE_WIDTH = 8

PLATE_AMOUNT = 10

PLATE_START_Y = SCREEN_HEIGHT / 2 + PLATE_WIDTH * PLATE_AMOUNT + 10

CENTER_HEIGHT = SCREEN_HEIGHT / 2

colorArray = []

pole1Items = []
pole2Items = []
pole3Items = []

poles = [
    pole1Items,
    pole2Items,
    pole3Items
]

hasFinished = 0
hasInit = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
running = True

def DrawPoles():
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH / 3, CENTER_HEIGHT, POLE_WIDTH, POLE_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH / 2, CENTER_HEIGHT, POLE_WIDTH, POLE_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH / 2 + SCREEN_WIDTH / 6, CENTER_HEIGHT, POLE_WIDTH, POLE_HEIGHT))
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2 + POLE_HEIGHT), (SCREEN_WIDTH / 2 + SCREEN_WIDTH / 6 + POLE_WIDTH - 1, SCREEN_HEIGHT / 2 + POLE_HEIGHT), POLE_WIDTH)

def InitColors():
    for _ in range(0, PLATE_AMOUNT):
        colorArray.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

def DrawPlates(flag):
    screen.fill("White")
    DrawPoles()
    if(flag == 1):
        for i in range(len(poles[0])):
            pygame.draw.rect(screen, colorArray[i - 1], (SCREEN_WIDTH / 3 - poles[0][i][1] / 2 + POLE_WIDTH / 2, PLATE_START_Y - i * PLATE_WIDTH, poles[0][i][1], PLATE_WIDTH))
    else:
        for i in range(len(poles[0])):
            pygame.draw.rect(screen, colorArray[i - 1], (SCREEN_WIDTH / 3 - poles[0][i][1] / 2 + POLE_WIDTH / 2, PLATE_START_Y - i * PLATE_WIDTH, poles[0][i][1], PLATE_WIDTH))
        for i in range(len(poles[1])):
            pygame.draw.rect(screen, colorArray[i - 1], (SCREEN_WIDTH / 2 - poles[1][i][1] / 2 + POLE_WIDTH / 2, PLATE_START_Y - i * PLATE_WIDTH, poles[1][i][1], PLATE_WIDTH))
        for i in range(len(poles[2])):
            pygame.draw.rect(screen, colorArray[i - 1], (SCREEN_WIDTH / 2 + SCREEN_WIDTH / 6 - poles[2][i][1] / 2 + POLE_WIDTH / 2, PLATE_START_Y - i * PLATE_WIDTH, poles[2][i][1], PLATE_WIDTH))

    pygame.display.flip()
    pygame.time.delay(200)

def InitPlates():
    width = 100
    for i in range(0, PLATE_AMOUNT):

        poles[0].append([i, width, 1])

        width -=10

    DrawPlates(1)

def MovePlate(fra, to):
    index = poles[fra].index(poles[fra][len(poles[fra]) -1])
    v = poles[fra].pop(index)
    print(F"{v} ({fra +1}) -> {to +1}")
    pygame.display.flip()
    poles[to].append(v)
    poles[to].sort()
    DrawPlates(0)

def Hanoi(p1, p2, p3, n):
    if(n == 1):
        print(F"{p1 +1} -> {p3 +1}")
        MovePlate(p1, p3)
    else:
        Hanoi(p1, p3, p2, n -1)
        print(F"{p1 +1} -> {p2 +1}")
        MovePlate(p1, p3)

        Hanoi(p2, p1, p3, n -1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif(event.type == pygame.KEYUP):
            if(event.unicode == "s"):
                hasFinished = 1
            print(event)
    
    if(hasInit == 0):
        screen.fill("White")
        colorArray = []
        InitColors()
        InitPlates()
        
        hasInit = 1

    if(hasFinished == 1):

        Hanoi(0, 1, 2, PLATE_AMOUNT)

        hasFinished = 0

    pygame.display.flip()

    clock.tick(60)