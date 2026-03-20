class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator in floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator in floor: {self.current_floor}")

    def go_to_floor(self, number):
        while self.current_floor > number:
            self.floor_down()
        while self.current_floor < number:
            self.floor_up()


class Building:
    def __init__(self, bottom_floor, top_floor, building_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(building_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, target_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(target_floor)
        
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)