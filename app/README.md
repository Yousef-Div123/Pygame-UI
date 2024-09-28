# PYGAME GUI EXT

**PYGAME GUI EXT** is a Python package that simplifies adding UI elements to a Pygame window by organizing them in a flexible grid layout. It provides ready-to-use components like buttons and labels that can be positioned easily in the window by specifying their grid coordinates and dimensions.

## Features

- **Grid Layout System**: Divide the window into a customizable grid, making it easy to position and resize UI elements.
- **Buttons and Labels**: Pre-built UI elements to speed up development, with customizable text and styles.
- **Flexible Element Placement**: Each element's position and size within the grid are specified by the number of blocks it spans in both width and height, offering precise control over layout and responsive features.

## Installation

You can install the package using pip:

```bash
pip install PYGAME_GUI_EXT
```

## How It Works

1. **Define a Grid**: You define the grid dimensions (rows and columns) when creating your window.
2. **Add UI Elements**: You can add buttons and labels by specifying their position in the grid and how many blocks they cover.
3. **Customize Elements**: Each UI element can be customized for appearance and behavior, making it easy to create interactive interfaces.

## Usage Example

Here’s a quick example to get you started:

```python
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

    pygame.display.update()
```
## Containers

1. **Grid**:
The main container that divides the window into a grid.

    **Variables:**
    - ***window(Surface):*** the surface where to apply the grid. 
    - ***numberOfCols(int):*** total number of columns in the grid. 
    - ***numberOfRows(int):*** total number of rows in the grid. 
    - ***blockWidth(float):*** the width of each block in the grid. 
    - ***blockHeight(float):*** the height of each block in the grid. 
    - ***children(list):*** list of components inside the grid.  

    **methods**:
    - ***Grid(window, numberOfCols, numberOfRows)***
        - window(Surface): the surface where to apply the grid.
        - numberOfCols(int): total number of columns in the grid.
        - numberOfRows(int): total number of rows in the grid.

    - ***showGrid()***
        - draws grid lines to window object to facilitate the development process.

    - ***addChild(child, startPos, colSpan, rowSpan)***
        - child(GuiElement): the element of which extends GuiElement to be added to children list.
        - colSpan(int): the number of columns that the child should acquire(the width of the child).
        - rowSpan(int): the number of rows that the child should acquire(the height of the child).

    - ***render()***
        - draws all children to window.

    - ***checkEvent(event)***
        - event(Event): the event to be handeled by each child.
        - The function is responsible for processing Pygame events (like mouse clicks, key presses, etc.) and passing them to the relevant UI elements within the grid.
        - Example Scenario: If a MOUSEBUTTONDOWN event occurs, the checkEvent(event) function could determine whether the click happened within the button's bounds and, if so, trigger the button's action.

## Components

1. **BasicButton**:
A clickable button that can trigger custom actions. You can specify the button text, dimensions, and an action to execute when clicked.

    **Variables:**
    - ***text(String):*** the text to be displayed inside the button. 
    - ***action(function):*** the callback function to be called when the button is clicked. 
    - ***color(tupel):*** the color of the button in rgb form. example: (0, 0, 0) -> black color 
    - ***textColor(tupel):*** the color of the button text in rgb form. example: (0, 0, 0) -> black color 
    - ***fontName(String), default = None:*** the name of the font for the button text. 

2. **BasicLabel**:
A simple text label that can be displayed at a specified location in the grid.

    **Variables:**
    - ***text(String):*** the text to be displayed. 
    - ***color(tupel):*** the color of the text in rgb form. example: (0, 0, 0) -> black color 
    - ***fontName(String), default = None:*** the name of the font for the text. 

    **Methods:**
    - ***setText(text)***
        - text(String): the text to be displayed. 

## Contributing
Contributions are welcome! If you'd like to add new features, fix bugs, or improve documentation, feel free to open a pull request.

## License

This project is licensed under the MIT License. It uses Pygame, which is licensed under the LGPL. Please refer to the Pygame documentation for more details on its licensing.


