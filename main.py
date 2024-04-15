import pygame
from pygame_UI.Button import Button
from pygame_UI.Label import Label

pygame.init()

WIN_WIDTH =800
WIN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Main")

run = True
def sayHello():
    print("Hello")



label1 = Label(10, 10, 50, "Test", RED, "comicsans")
label1.centerText(WIN_WIDTH)

label2 = Label(10, 10 + label1.getHeight(), 50, "Test2", RED, 'comicsans')
label2.centerText(WIN_WIDTH)



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.draw.rect(win, WHITE, (0, 0, WIN_WIDTH, WIN_HEIGHT))

    label1.draw(win)
    label2.draw(win)

    pygame.display.update()


