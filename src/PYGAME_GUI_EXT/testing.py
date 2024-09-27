import pygame
import Container
import Component.Elements as Elements

pygame.init()
# window
WIN = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Testing")

#Grid 
grid = Container.Grid(WIN, 30, 30)

def start():
    print("start")

def menu():
    print("menu")

grid.addChild(Elements.BasicButton("Start", start, (255, 0, 0), (0, 0, 0)), (7, 20), 6, 2)
grid.addChild(Elements.BasicButton("menu", menu, (0, 0, 255), (0, 0, 0)), (17, 20), 6, 2)
# grid.addChild(Elements.TestingBox((0, 255, 0)), (15, 20), 5, 2)


def drawWindow():
    pygame.draw.rect(WIN, (255, 255, 255), (0, 0, 600, 700))
    grid.render()
    # grid.showGrid()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        grid.checkEvent(event)

    drawWindow()
    pygame.display.update()