STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle, Screen


class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.setup()
        self.movement()

        self.screen = screen


    def setup(self):
        self.hideturtle()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def movement(self):
        self.screen.listen()
        self.screen.onkey(fun=self.move, key="Up")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def beyond_screen(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.hideturtle()
            self.goto(STARTING_POSITION)
            self.showturtle()
            return True

    def car_contact(self, car_list):
        for car in car_list:
            if self.distance(car) <= 30:
                # Correct floor and ceil calculation
                floor = car.ycor() - 20
                ceil = car.ycor() + 20
                if floor <= self.ycor() <= ceil:
                    return True
        return False

