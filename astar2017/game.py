# Import a library of functions called 'pygame'
import pygame
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 10
COLS = 10
WIDTH = 30
HEIGHT = 30


def main():
    '''main function'''
    pygame.init()
    # Define the colors we will use in RGB format
    SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
    SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
    # Set the height and width of the SCREEN

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    SEARCH_SPACE = Graph([ROWS, COLS])

    NODES = {}
    for i in range(ROWS):
        for j in range(COLS):
            node = SEARCH_SPACE.get_node([i, j])
            drawnode = DrawableNode(node)
            NODES[str(i), ",", str(j)] = drawnode
    
    # set the neighbors
    pygame.display.set_caption("PyStar Year 1 2017")

    # Loop until the user clicks the close button.
    DONE = False
    CLOCK = pygame.time.Clock()

    pygame.font.init()
    while not DONE:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        CLOCK.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                DONE = True  # Flag that we are DONE so we exit this loop

        # All drawing code happens after the for loop and but
        # inside the main while DONE==False loop.

        # Clear the SCREEN and set the SCREEN background
        SCREEN.fill(WHITE)
        # Draw a circle
        for i in NODES:
            i.draw(SCREEN)

        CURRENT = NODES[1]
        for i in CURRENT.adjacents:
            i.color = GREEN

        # Go ahead and update the SCREEN with what we've drawn.
        # This MUST happen after all the other drawing commands.
        bg = pygame.Surface(
            (SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
        bg.fill(BLACK)
        textrect = bg.get_rect()
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()

if __name__ == "__main__":
    main()