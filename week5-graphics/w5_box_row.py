#this code is the assignment of "box row"
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range (N_BOXES):
        x1 = 0 + i * BOX_SIZE
        y1 = CANVAS_HEIGHT - BOX_SIZE
        x2 = (i+1) * BOX_SIZE
        y2 = CANVAS_HEIGHT
        canvas.create_rectangle(x1, y1, x2, y2, 'white', 'black' )


if __name__ == '__main__':
    main()
    