from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    BRICKS_IN_BASE = 14     # The number of bricks in the base
    start_x = (CANVAS_WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH))/2 #make sure the pyramid is in the middle
    layer = 1 #to define the layer

    #this will create the following lines above
    while BRICKS_IN_BASE > 0:
        
        #this will create one base line of bricks
        for i in range(BRICKS_IN_BASE):
            #this will create a single brick
            create_brick(
                canvas, 
                start_x + i * BRICK_WIDTH, #for next brick, add a new width
                CANVAS_HEIGHT - BRICK_HEIGHT * layer, #for the next line, substract a height
                'yellow'
            )
        start_x = start_x + 15  #move to the next line and move inside 15
        layer = layer + 1    #move to the next line
        BRICKS_IN_BASE = BRICKS_IN_BASE - 1  #the next line's bricks is substracted by 1
    
#this will create a single brick
def create_brick(canvas, x1, y1, color):
    #x2 and y2 are defined by the width and height of one brick  
    x2 = x1 + BRICK_WIDTH
    y2 = y1 + BRICK_HEIGHT

    #this will create a brick with black outline
    canvas.create_rectangle(
        x1,
        y1,
        x2, #x2 = x1 + BRICK_WIDTH
        y2, #y2 = y1 + BRICK_HEIGHT
        color, #the filled color can be defined by the user
        'black'
    )


if __name__ == '__main__':
    main()
