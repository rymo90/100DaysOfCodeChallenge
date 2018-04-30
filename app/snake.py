''' snake Game part 1
'''
''' #1 import some stuff'''
import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP
from random import randint

''' #2 Defind some variables '''
WIDTH= 35 # total game cell width and heigt
HEIGHT= 20
MAX_X= WIDTH -2 #set max inside the game, so that the snake wont hit the border
MAX_Y = HEIGHT - 2
SNAKE_LENGTH= 5
SNAKE_X= SNAKE_LENGTH +1
SNAKE_Y= 3
TIMEOUT= 100 # this controll the speed of the game
'''#3 make snake object '''
class Snake(object):
    def __init__(self):
        self.x= 'Hisss!'
    def method_a(self,foo):
        print (self.x + ' ' + foo)
snake= Snake()
snake.method_a('Says the snake')
