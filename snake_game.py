from turtle import *
import random
from random import randrange
from freegames import square, vector

colorsSnake = random.choice(['blue', 'green', 'black','goldenrod','pink'])
colorsFood = random.choice(['purple','orange','deep sky blue','light salmon','saddle brown'])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insidex(x):
  return -200 < x < 190

def insidey(y):
  return -200 < y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorsSnake)

    square(food.x, food.y, 9, colorsFood)
    update()
    ontimer(move, 100)

def moveFood():
  if inside(food):
    r=random.randint(0,3)
    if r==0:
      if not insidex(food.x+1*10):
        None
      else:
        food.x += 1 * 10
    elif r==1:
      if not insidey(food.y+1*10):
        None
      else:
        food.y += 1 * 10
    elif r==2:
      if not insidex(food.x-1*10):
        None
      else:
        food.x-=1*10
    else:
      if not insidey(food.y-1*10):
        None
      else:
        food.y-=1*10
  ontimer(moveFood,500)
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
