from pico2d import *

open_canvas()

boy=load_image('character.png')
grass=load_image('grass.png')

def move_top():
    print("Move top")
    for x in range(770,0,-10):
        draw_boy(x,550)
    pass

def move_bottom():
    print("Move bottom")
    for x in range(400, 770, 10):
        draw_boy(x, 90)
    pass

def move_left():
    print("Move left")
    for y in range(550, 90, -10):
        draw_boy(0, y)
    pass

def move_right():
    print("Move right")
    for y in range(90, 550, 10):
        draw_boy(770, y)
    pass

def move_bottom1():
    print("Move bottom1")
    for x in range(0, 400, 10):
        draw_boy(x, 90)

def move_rectangle():
    print("Move rectangle")
    move_bottom()
    move_right()
    move_top()
    move_left()
    move_bottom1()
    pass

def move_triangle_right1():
    print("Move triangle right1")
    pass

def move_triangle_up():
    print("Move triangle up")
    pass

def move_triangle_down():
    print("Move triangle down")
    pass

def move_triangle_right2():
    print("Move triangle right2")
    pass

def move_triangle():
    print("Move triangle")
    move_triangle_right1()
    move_triangle_right2()
    move_triangle_up()
    move_triangle_down()
    pass


def move_circle():
    print("Move circle")
    r = 200
    for deg in range(-90,270):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw(400, 30)
    update_canvas()
    delay(0.05)


while True:
    move_triangle()
    move_circle()
    move_rectangle()
    break
    pass


close_canvas()
