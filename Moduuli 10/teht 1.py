class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def floor_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print(f"Elevator in floor: {self.floor}")

    def floor_down(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print(f"Elevator in floor: {self.floor}")

    def go_to_floor(self, number):
        while self.floor > number:
            self.floor_down()
        while self.floor < number:
            self.floor_up()