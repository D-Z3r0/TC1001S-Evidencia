from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
winWriter = Turtle(visible=False)
win = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global win
    "Update mark and hidden tiles based on tap."
    tap.counter += 1
    tapsString = "Number of taps %s" %tap.counter
    title(tapsString)
    print("Number of taps: ", tap.counter)

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        win += 1
        print(win)

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+27,y)
        color('black')
        write(tiles[mark],align = 'center',font=('Arial', 30, 'normal'))

    if win == 32:
        winWriter.setposition(0,0)
        winWriter.color('purple')
        winWriter.write('"YOU WIN"',align='center',font=('Arial', 50, 'normal'))
        onscreenclick(None)
        done()  
        return
    
    update()
    ontimer(draw, 100)


tap.counter = 0

shuffle(tiles)
setup(420,420,370,0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

#Innovation
#Instead of using numbers, colors appear when the tiles are flipped. We believe that it is easier to memorize colors than numbers.
