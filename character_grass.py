from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)


while(1):
    x = 0
    y = 90
    while(x<760):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 5
        delay(0.01)
    while(y<550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 5
        delay(0.01)
    while(x>10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 5
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 5
        delay(0.01)

close_canvas()
