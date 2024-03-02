import threading
import random
import time

class Gate:
    def __init__(self, name, max_cars):
        self.name = name
        self.max_cars = max_cars
        self.cars_waiting = 0
        self.lock = threading.Lock()

    def let_in(self):
        while True:
            with self.lock:
                if self.cars_waiting > 0:
                    cars_to_let_in = min(self.cars_waiting, self.max_cars)
                    self.cars_waiting -= cars_to_let_in
                    print(f"{self.name} letting in {cars_to_let_in} cars. {self.cars_waiting} cars waiting.")
                else:
                    print(f"No cars waiting at {self.name}")
            time.sleep(1)

    def add_car(self):
        with self.lock:
            self.cars_waiting += 1
            print(f"Car arrived at {self.name}. {self.cars_waiting} cars waiting.")

class CarGenerator(threading.Thread):
    def __init__(self, gate):
        threading.Thread.__init__(self)
        self.gate = gate

    def run(self):
        while True:
            time.sleep(random.randint(1, 3))
            self.gate.add_car()

gateA = Gate("GateA", 5)
gateB = Gate("GateB", 5)

car_genA = CarGenerator(gateA)
car_genB = CarGenerator(gateB)

car_genA.start()
car_genB.start()

while True:
    gateA.let_in()
    gateB.let_in()