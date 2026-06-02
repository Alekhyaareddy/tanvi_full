from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

c = Counter('hits', 'Website Hits')

@app.route('/')
def home():
    c.inc()
    return "Hello World"

@app.route('/metrics')
def metrics():
    return generate_latest()

app.run(host='0.0.0.0', port=5000)