import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    global cars, game_is_on
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.moving_cars()
        cars.remove_car_from_list()
        if player.beyond_screen():
            cars.hide_cars() # HIDES previous car_list, may bug, nag pause mga cars if player.beyond_screen()
            create_cars()
            score.lvl += 1
            score.show_level()
        if player.car_contact(cars.car_list):
            score.game_over()
            game_is_on = False # ----- > Exit loop


#Global Variables
game_is_on = True
screen = Screen()
player = Player(screen)
cars = None
score = Scoreboard()

#Functions
def screen_setup():
    screen.setup(width=600, height=600)
    screen.tracer(0)

def create_cars():
    global cars
    cars = CarManager()
    screen.update()

#Call
screen_setup()
create_cars()
main()
screen.mainloop()
