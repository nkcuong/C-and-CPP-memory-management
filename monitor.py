# Description: This file is the main file for the web application. It uses flask and socketio to create a web application that monitors the producer consumer queue.
# Test: Run this file and go to http://127.0.0.1:5001/ to see the web application.




from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from ProducerConsumerOOP import ProducerConsumerQueue, Producer, Consumer
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)
pcq = ProducerConsumerQueue(100)
producer1 = Producer("P1", pcq, 1000, 5)
producer2 = Producer("P2", pcq, 1000, 3)
consumer1 = Consumer("C1", pcq, 1000, 6)
consumer2 = Consumer("C2", pcq, 1000, 4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queue')
def queue():
    return jsonify(list(pcq.queue.queue))

@socketio.on('start')
def handle_start():
    threading.Thread(target=monitor).start()
    producer1.start()
    producer2.start()
    time.sleep(5)
    consumer1.start()
    consumer2.start()
    

def monitor():
    while True:
        socketio.emit('queue', "Length: "+ str(pcq.queue.qsize()) + str(list(pcq.queue.queue)))
        socketio.emit('producers', str(producer1.name) + " produced: " + str(producer1.lastProduced) + " counter : " + str(producer1.counter) + " -- " + str(producer2.name) + " produced: " + str(producer2.lastProduced) + " counter :  " + str(producer2.counter))
        socketio.emit('consumers', str(consumer1.name) + " consumed: " + str(consumer1.lastConsumed) + " counter : " + str(consumer1.counter)  + " -- " + str(consumer2.name) + " consumed: " + str(consumer2.lastConsumed) +  " counter : " + str( consumer2.counter))
        time.sleep(0.5)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
   # socketio.run(app, debug=True)