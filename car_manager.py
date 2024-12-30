from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
        self.forward(STARTING_MOVE_DISTANCE)

    def setup(self):
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)

        self.set_random_location()

        self.showturtle()

    def move(self):
        self.forward(MOVE_INCREMENT)

    def set_random_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-240, 280) # ----> -240 para walang cars after spawn
        self.goto(x,y)

class CarManager(Car):
    def __init__(self):
        # super().__init__() # ------------> COMMENT, PARA MAWALA UNG ISANG CAR NA HINDI GUMAGALAW
        self.starting_create_list_of_cars()

    def starting_create_list_of_cars(self):
        self.car_list = []
        for car in range(0, 20): #Create 20 cars
            car = Car()
            self.car_list.append(car)

    def create_cars_at_edge_screen(self):
        car = Car()
        car.setx(280)
        self.car_list.append(car)

    def moving_cars(self):
        for car in self.car_list:
            car.move()

    def remove_car_from_list(self):
        for car in self.car_list:
            if car.xcor() <= -310:
                car.hideturtle()
                self.car_list.remove(car)
                del car
                self.create_cars_at_edge_screen()

    def hide_cars(self):
        for car in self.car_list:
            car.hideturtle()


