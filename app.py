import time
from flask import Flask

app = Flask(__name__)
t = time.time()


@app.route('/')
def hello_world():
    return str(time.ctime(t))
