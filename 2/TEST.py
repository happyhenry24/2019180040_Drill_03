from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('CIRCLE')
    r, cx, cy = 300, 800//2, 600//2
    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x,y)

def run_top():
    print('TOP')
    for x in range(0, 800, 10):
        draw_boy(x, 600)

def run_right():
    print('RIGHT')
    for y in range(600, 0, -10):
        draw_boy(790,y)

def run_bottom():
    print('BOTTOM')
    for x in range(800, 0, -10):
        draw_boy(x, 0)

def run_left():
    print('LEFT')
    for y in range(0, 600, 10):
        draw_boy(0, y)

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()

def run_tritop():
    print('TRITOP')
    for i in range(200, 400, 10): 
        draw_boy(i, i) 

def run_triright():
    print('TRIRIGHT')
    for i in range(400, 600, 10): 
        draw_boy(i, 800 - i) 

def run_trileft():
    print('TRILEFT')
    for i in range(600, 200, -10): 
        draw_boy(i, 200) 

def run_triangle():
    print('TRIANGLE')
    run_tritop()
    run_triright()
    run_trileft()

while True:
    run_circle()
    run_rectangle()
    run_triangle()

