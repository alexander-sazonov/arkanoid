import pgzrun

TITLE = 'Arkanoid Clone'
WIDTH = 800
HEIGHT = 500
bar_list = []
ball_x_speed = 1
ball_y_speed = 1
def place_bars(x, y):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor('brick.png')
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bar_list.append(bar)
x = 120
y = 100
for i in range(3):
    place_bars(x,y)
    y+= 50
paddle = Actor('paddle.png')
paddle.x = 120
paddle.y = 420

ball = Actor('ball.png')
ball.x = 30
ball.y = 300
def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if ball.x >= WIDTH or ball.x <= 0:
        ball_x_speed *= -1
    if ball.y >= HEIGHT or ball.y <= 0:
        ball_y_speed *= -1
def draw():
    screen.clear()
    paddle.draw()
    ball.draw()
    for bar in bar_list:
        bar.draw()

def update():
    update_ball()
    if keyboard.left:
        paddle.x -= 5
    if keyboard.right:
        paddle.x += 5

pgzrun.go()


