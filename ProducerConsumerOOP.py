import queue
import threading
import time
import random
from queue import Empty



class Producer(threading.Thread):
	def __init__(self, pcq, n, velocity):
		threading.Thread.__init__(self)
		self.pcq = pcq
		self.n = n
		self.counter = 0
		self.velocity = velocity

	def run(self):
		while self.counter < 5:
			time.sleep(self.velocity)
			i = random.randint(1, 1000)
			self.pcq.produce(i, self.n)
			self.counter += 1


class Consumer(threading.Thread):
	def __init__(self, pcq, m, velocity):
		threading.Thread.__init__(self)
		self.pcq = pcq
		self.m = m
		self.counter = 0
		self.velocity = velocity

	def run(self):
		while self.counter < 10:
			time.sleep(self.velocity)
			self.pcq.consume(self.m)
			# if no more to consume, break
			self.counter += 1


class ProducerConsumerQueue:
	def __init__(self, capacity):
		self.queue = queue.Queue(capacity)
		print("Queue created with capacity: " + str(capacity) + "\n")

	def produce(self, item, n):
		self.queue.put(item)  # Blocks if queue is full
		print("Producer " + str(n) + " produced: " + str(item) + " - queue: " + str(self.queue.queue) + "\n")
	

	def consume(self, n):
		try:
			item = self.queue.get(block=False)  # Raises queue.Empty if queue is empty
			print("Consumer " + str(n) + " consumed: " + str(item) + " - queue: " + str(self.queue.queue) + "\n")
			return item
		except Empty:
			print("Consumer " + str(n) + " stopping: no more items to consume")
			return None


def start_producers():
	global producers
	producers = [Producer(pcq, n, 1) for n in range(1, 5)] # 4 producers with velocity 1
	for producer in producers:
		producer.start()


def start_consumers():
	global consumers
	consumers = [Consumer(pcq, m, 2) for m in range(1, 3)] # 2 consumers with velocity 2
	for consumer in consumers:
		consumer.start()



	
pcq = ProducerConsumerQueue(100)
start_producers()
time.sleep(2)  # Let the producers produce for 2 seconds
start_consumers()








