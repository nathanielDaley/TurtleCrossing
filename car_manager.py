import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_X_POSITION = 320


class CarManager:
    def __init__(self):
        self.cars = []

        for _ in range(21):
            random_x = random.randint(-56, 56)
            random_y = random.randint(-52, 52)
            self.create_car((random_x * STARTING_MOVE_DISTANCE, random_y * STARTING_MOVE_DISTANCE))

    def create_car(self, position):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setposition(position)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() - MOVE_INCREMENT < -300:
                random_y = random.randint(-52, 52)
                car.setposition(INITIAL_X_POSITION, random_y * STARTING_MOVE_DISTANCE)

            car.setposition(car.xcor() - MOVE_INCREMENT, car.ycor())

    def check_collision(self, position):
        collision = False
        for car in self.cars:
            car_top_y = car.ycor() + 20
            car_bottom_y = car.ycor() - 20
            car_right_x = car.xcor() + 10
            car_left_x = car.xcor() - 10
            if (car_left_x <= position[0] <= car_right_x
                    and car_top_y >= position[1] >= car_bottom_y):
                collision = True

        return collision