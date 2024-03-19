from turtle import Turtle, Screen
from time import sleep

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.tracer(0)
        self.position = (0, 0)
        self.snakes = []

        for i in range(3):
            self.position = self.create_snake(self.position)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def create_snake(self, position):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.up()
        position = (position[0]-DISTANCE, position[1])
        new_body.setpos(position)
        self.snakes.append(new_body)
        return position

    def move(self):
        snake_head = self.snakes[0]
        for snake in reversed(self.snakes):
            if snake == snake_head:
                snake.forward(DISTANCE)
            elif snake != snake_head:
                snake_ahead = self.snakes[self.snakes.index(snake)-1].pos()
                snake.setpos(snake_ahead)
        else:
            self.screen.update()
            sleep(0.1)
    
    def reset(self):
        for snake in self.snakes:
            snake.hideturtle()
        else:
            self.snakes.clear()

        self.position = (0, 0)
        for i in range(3):
            self.position = self.create_snake(self.position)