from flask import Flask, render_template, jsonify

app = Flask(__name__)
pcq = ProducerConsumerQueue(5)
producer = Producer(pcq, "Producer")
consumer = Consumer(pcq, "Consumer")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queue')
def queue():
    return jsonify(list(pcq.queue.queue))

if __name__ == '__main__':
    producer.start()
    consumer.start()
    app.run(debug=True)