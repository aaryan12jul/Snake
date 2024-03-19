from turtle import Turtle, Screen
from random import randint as num

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.register_shape("apple.gif")
        self.shape("apple.gif")
        self.penup()
        self.refresh()
    
    def refresh(self):
        self.goto(num(-250, 250), num(-250, 250))