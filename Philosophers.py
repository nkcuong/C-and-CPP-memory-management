# Description: This is a simple implementation of the dining philosophers problem in Python.
import random
import threading
from time import sleep

#define monitor class for monitoring the number of times each philosopher in 5 philosophers eats
class Monitor():
    def __init__(self):
        self.eat_count = [0, 0, 0, 0, 0]
        self.round_eaten = [False, False, False, False, False]
        self.lock = threading.Lock()

    def increment_eat_count(self, philosopher):
        with self.lock:
            self.eat_count[philosopher] += 1
            self.round_eaten[philosopher] = True

    def get_eat_count(self, philosopher):
        return self.eat_count[philosopher]

    def has_eaten_this_round(self, philosopher):
        return self.round_eaten[philosopher]

    def reset_round(self):
        with self.lock:
            if all(self.round_eaten):
                self.round_eaten = [False, False, False, False, False]
	
theMonitor = Monitor()

class Philosopher(threading.Thread):
	def __init__(self, name, left_fork, right_fork):
		threading.Thread.__init__(self)
		self.left_fork = left_fork
		self.right_fork = right_fork
		self.name = name

	def run(self):
		while True:
			self.think()
			if not theMonitor.has_eaten_this_round(int(self.name.split('-')[1])): 
				self.eat()
			theMonitor.reset_round()

	def think(self):
		# Implement the thinking logic here
		print(f"{self.name} is thinking")
		sleep(random.randint(1, 5))
		pass

	def eat(self):
		# Acquire the forks in a specific order to avoid deadlock
		self.left_fork.lock.acquire()
		self.right_fork.lock.acquire()
		# Implement the eating logic here
		print(f"{self.name} is EATING")
		sleep(random.randint(1, 5))
		theMonitor.increment_eat_count(int(self.name.split("-")[1]))
		print(f"{self.name} has eaten {theMonitor.get_eat_count(int(self.name.split('-')[1]))} times") 
		print(theMonitor.get_eat_count(0), theMonitor.get_eat_count(1), theMonitor.get_eat_count(2), theMonitor.get_eat_count(3), theMonitor.get_eat_count(4))
		# Release the locks
		self.left_fork.lock.release()
		self.right_fork.lock.release()



# define the fork
class Fork():
	def __init__(self, name):
		self.name = name
		self.lock = threading.Lock()
	def __str__(self):
		return self.name
	


# Create the forks
forks = [Fork(f"Fork-{i}") for i in range(5)]
for fork in forks:
	print(fork)
	


# Create the philosophers
philosophers = []
for i in range(5):
	left_fork = forks[i]
	right_fork = forks[(i + 1) % 5]
	philosopher = Philosopher("Philosopher-"+str(i), left_fork, right_fork)
	philosophers.append(philosopher)
for philosopher in philosophers:
	print(philosopher.name, philosopher.left_fork, philosopher.right_fork)

# Start the philosophers
for philosopher in philosophers:
	philosopher.start()

# Wait for all philosophers to finish
for philosopher in philosophers:
	philosopher.join()