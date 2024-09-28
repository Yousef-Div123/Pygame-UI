import pygame
import PYGAME_GUI_EXT.src.Component.Elements as Elements
import PYGAME_GUI_EXT.src.Container as Container

pygame.init()
# window
WIN = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Testing")

#Grid with 10 cols and 10 rows
grid = Container.Grid(WIN, 10, 10)

# action: callback function runs when the button is clicked
def start():
    print("start")

# BasicButton(text, action, buttonColor, textColor)
button = Elements.BasicButton("Start", start, (255, 0, 0), (0, 0, 0))
# BasicLabel(text, textColor)
label = Elements.BasicLabel('hello', (255, 0, 0))

# adding elements to grid grid.addChild(element, (colNumber, rowNumber), colSpan, rowSpan)
grid.addChild(button, (2, 2), 2, 2)
grid.addChild(label, (5, 2), 3, 2)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # handle events for each element in the grid
        grid.checkEvent(event)

    pygame.draw.rect(WIN, (255, 255, 255), (0, 0, 600, 700))
    # draws every element in the grid to the screen
    grid.render()
    grid.showGrid()

    pygame.display.update()
