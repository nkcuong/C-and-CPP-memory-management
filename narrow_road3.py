import threading
import time
import random

class Gate:
	def __init__(self, name, max_cars):
		self.name = name
		self.max_cars = max_cars
		self.cars_passed = 0
		self.cars_waiting = []
		self.lock = threading.Lock()
		self.condition = threading.Condition()

	def open_gate(self):
		with self.lock:
			while self.cars_passed < self.max_cars and self.cars_waiting:
				car = self.cars_waiting.pop(0)
				print(f"{car} passed through {self.name} gate")
				self.cars_passed += 1
				time.sleep(1)  # Simulate time to pass through the gate

			if self.cars_passed == self.max_cars:
				print(f"{self.name} gate is full, signaling the other gate to reverse")
				self.condition.notify()

	def add_car(self, car):
		with self.lock:
			self.cars_waiting.append(car)
			print(f"{car} is waiting at {self.name} gate")

	def wait_for_signal(self):
		with self.condition:
			self.condition.wait()

def generate_car(gate):
	while True:
		time.sleep(random.randint(1, 100))
		car = f"Car-{random.randint(1, 100)}"
		gate.add_car(car)

def main():
	left_gate = Gate("Left", 20)
	right_gate = Gate("Right", 20)

	left_thread = threading.Thread(target=generate_car, args=(left_gate,))
	right_thread = threading.Thread(target=generate_car, args=(right_gate,))

	left_thread.start()
	right_thread.start()

	while True:
		left_gate.open_gate()
		left_gate.wait_for_signal()

		time.sleep(3)  # Time to release the road

		right_gate.open_gate()
		right_gate.wait_for_signal()

if __name__ == "__main__":
	main()