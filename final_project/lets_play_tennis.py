'''
Welcome, this is a tennis game!

player can control the paddle with mouse and hit the ball 
the ball will bounce between the paddle and wall
the speed of the ball will change when you get a higher score
 
'''
from graphics import Canvas
import random

#Initial set of canvas, paddle and tennis ball    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 60
TENNIS_WIDTH = 30
TENNIS_HEIGHT = 30

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    level = 1
    score = 0

    #Initial Setup
    game_mess = canvas.create_text(80, 100, "Welcome to the tennis game!", font_size = 20, color = "blue") 
    level1_mess = canvas.create_text(170, 180, "Level 1", font_size = 20, color = "red")     

    #wait the user to click
    canvas.wait_for_click()
    canvas.clear()

    #create the wall, paddle and tennis
    wall = canvas.create_rectangle(0, 0, CANVAS_WIDTH, 100, "brown")
    wall_mess = canvas.create_text(160, 40, "WALL", font_size = 20)
    score_mess = canvas.create_text(10, 10, f"Your Score: {score}", font_size = 15, color = "white")  

    paddle = draw_paddle(canvas, random.randint(0,CANVAS_WIDTH-PADDLE_WIDTH), CANVAS_HEIGHT - PADDLE_HEIGHT - 10)
    tennis = draw_tennis(canvas, random.randint(0,CANVAS_WIDTH-TENNIS_WIDTH), 105)

    #paddle move with the mouse
    #tennis move
    move_paddle_tennis(canvas, paddle, tennis, score_mess, score)
  
#create a paddle
def draw_paddle(canvas, left_x, top_y):
    return canvas.create_image_with_size(left_x, top_y, PADDLE_WIDTH, PADDLE_HEIGHT, 'img/racket.png')

#create a tennis ball
def draw_tennis(canvas, left_x, top_y):
    return canvas.create_image_with_size(left_x, top_y, TENNIS_WIDTH, TENNIS_HEIGHT, 'img/tennis.png')

#make paddle move with the mouse
#constanly get the x position from the mouse
#and transfer mouse'x position to paddle
def move_paddle_tennis(canvas, paddle, tennis, score_mess, score):
    #Initial speed and direction of the tennis
    tennis_speed_x = 0.06 #Horizontal velocity
    tennis_speed_y = 0.06 #Vertical velocity
    has_collided = False
    while True:
        #MOVE PADDLE
        #change the x point of paddle from mouse position
        paddle_mouse_x = canvas.get_mouse_x()

        #make sure paddle will not exceed the canvas           
        if paddle_mouse_x > (CANVAS_WIDTH-PADDLE_WIDTH):  
            paddle_mouse_x = CANVAS_WIDTH - PADDLE_WIDTH
        
        #make the paddle move with the mouse every 20ms
        canvas.moveto(paddle, paddle_mouse_x, CANVAS_HEIGHT - PADDLE_HEIGHT - 10)
        canvas.sleep(20)       #refresh the x position of paddle every 20ms
        
        #MOVE TENNIS
        #Current position of the tennis ball
        tennis_x = canvas.get_left_x(tennis)
        tennis_y = canvas.get_top_y(tennis)

        #Make sure tennis will not exceed canvas
        #Scene1: tennis reach the left or right wall
        if tennis_x <= 0 or tennis_x >= (CANVAS_WIDTH - TENNIS_WIDTH):
            tennis_speed_x = -tennis_speed_x

        #Scene2: tennis reach top wall
        if tennis_y <= 100:
            tennis_speed_y = -tennis_speed_y

        #Scene3: tennis reach the paddle
        #if tennis_bottom_y_position is in [paddle_y_top_position, 1/2 paddle_y_top_position]
        #and tennis_left_x_positon is in [paddle_x_left_position + tennis width, paddle_x_right_position]
        #bounce success
        
        #define colliding
        is_colliding = (
            (tennis_x >= (paddle_mouse_x - TENNIS_WIDTH)) and
            (tennis_x <= (paddle_mouse_x + PADDLE_WIDTH)) and
            ((tennis_y + TENNIS_HEIGHT) >= (CANVAS_HEIGHT - PADDLE_HEIGHT - 10))
        )
        
        #make sure one bounce only score once
        if is_colliding:
            if not has_collided:
                tennis_speed_y = -abs(tennis_speed_y)
                #UPDATE SCORE
                score = update(canvas, score_mess, score)
                has_collided = True
        else:
            has_collided = False
            

        #Scene4: tennis exceed the canvas
        if tennis_y >= CANVAS_HEIGHT:
            canvas.create_text(120, 150, "Game Over!", font_size=30, color='red')
            canvas.create_text(150, 200, f"Your Score: {score}", font_size=20, color='red')
            break

        #change the position of tennis every 20ms
        canvas.move(tennis, tennis_speed_x, tennis_speed_y)       
        canvas.sleep(20)

#Update the score and score message
def update(canvas, score_mess, score):
    score += 15
    canvas.change_text(score_mess, f"Your Score: {score}")
    return score

if __name__ == '__main__':
    main()