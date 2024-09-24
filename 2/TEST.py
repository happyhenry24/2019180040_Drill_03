from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
while(x < 790):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x += 2
    delay(0.01)
    
while(y < 580):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(790, y)
    y += 2
    delay(0.01)

while(x > 10):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 580)
    x -= 2
    delay(0.01)

while(y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(0, y)
    y -= 2
    delay(0.01)
close_canvas()

