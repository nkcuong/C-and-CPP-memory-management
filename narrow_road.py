import threading
import time
import random

class NarrowRoad:
	def __init__(self, max_cars):
		self.max_cars = max_cars
		self.current_cars = 0
		#self.road_lock = threading.Lock()
		self.left_gate = threading.Semaphore(1)
		self.right_gate = threading.Semaphore(0)
		self.left_cars = 20
		self.right_cars = 20

	def left_gatekeeper(self):
		while True:
			if self.left_gate.acquire():
				while self.current_cars < self.max_cars and self.left_cars > 0:
					self.current_cars += 1
					self.left_cars -= 1
					print(f"   Car from left gate entered. Current cars: {self.current_cars}")
					time.sleep(1)
				self.right_gate.release()
				self.current_cars = 0
				time.sleep(3)

	def right_gatekeeper(self):
		while True:
			if self.right_gate.acquire():
				while self.current_cars < self.max_cars and self.right_cars > 0:
					self.current_cars += 1
					self.right_cars -= 1
					print(f"   Car from right gate entered. Current cars: {self.current_cars}")
					time.sleep(1)
				self.left_gate.release()
				self.current_cars = 0
				time.sleep(3)

	def left_car(self):
		while True:
			time.sleep(random.randint(1, 10))
			self.left_cars += 1
			print("Car from left side arrived. Number of cars: ", self.left_cars)


	def right_car(self):
		while True:
			time.sleep(random.randint(1, 10))
			self.right_cars += 1
			print("Car from right side arrived. Number of cars: ", self.right_cars)


if __name__ == "__main__":
	road = NarrowRoad(5)
	threading.Thread(target=road.left_gatekeeper).start()
	threading.Thread(target=road.right_gatekeeper).start()
	threading.Thread(target=road.left_car).start()
	threading.Thread(target=road.right_car).start()
