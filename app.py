import time, threading, requests, os
from flask import Flask

app = Flask(__name__)
t = time.time()
print(os.environ)

def keepAlive():
    while 1:
        y = requests.get('https://b234561.onrender.com/')
        time.sleep(666)


threading.Thread(target=keepAlive).start()


@app.route('/')
def hello_world():
    return str(time.ctime(t))
