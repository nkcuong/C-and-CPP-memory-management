import queue
import threading
import time
import random
from queue import Empty

class ProducerConsumerQueue:
	def __init__(self, capacity):
		self.queue = queue.Queue(capacity)
		print("Queue created with capacity: " + str(capacity) + "\n")

	def produce(self, item):
		self.queue.put(item)  # Blocks if queue is full
	
	def consume(self):
		try:
			# item = self.queue.get(block=False)  # Raises queue.Empty if queue is empty
			item = self.queue.get(block=True)
			return item
		except Empty:
			print("Consumer " + self.name + "stopping: no more items to consume")
			return None


class Producer(threading.Thread):
	def __init__(self, name, pcq, capacity, velocity):
		threading.Thread.__init__(self)
		self.name = name
		self.pcq = pcq
		self.capacity = capacity
		self.counter = 0
		self.velocity = velocity
		self.lastProduced = None

	def run(self):
		while self.counter < self.capacity:
			time.sleep(self.velocity)
			i = random.randint(1, 1000)
			self.pcq.produce(i)
			self.lastProduced = i
			print("Producer " + self.name + " produced: " + str(i) + " - queue: " + "len:" + str(self.pcq.queue.qsize()) + " - Content: " + str(self.pcq.queue.queue) + "\n")
			self.counter += 1


class Consumer(threading.Thread):
	def __init__(self, name, pcq, capacity, velocity):
		threading.Thread.__init__(self)
		self.name = name
		self.pcq = pcq
		self.capacity = capacity
		self.counter = 0
		self.velocity = velocity
		self.lastConsumed = None

	def run(self):
		while self.counter < self.capacity:
			time.sleep(self.velocity)
			i = self.pcq.consume()
			self.lastConsumed = i
			print("Consumer " + self.name + " consume: " + str(i) + " - queue: " + str(self.pcq.queue.queue) + "\n")
			# if no more to consume, break
			self.counter += 1


# test the whole thing
# main: uncomment following lines:
			
def start_producers():
	global producers
	producers = [Producer(str(n), pcq, 100, 2) for n in range(1, 5)] # 4 producers with velocity 1
	for producer in producers:
		producer.start()


def start_consumers():
	global consumers
	consumers = [Consumer(str(m), pcq, 100, 1.5) for m in range(1, 3)] # 2 consumers with velocity 2
	for consumer in consumers:
		consumer.start()


pcq = ProducerConsumerQueue(100)
start_producers()
time.sleep(2)  # Let the producers produce for 2 seconds
start_consumers()








