from flask import Flask, request
import time

app = Flask(__name__)
motion_time = None
proximity_time = None

@app.route('/motion', methods=['POST'])
def motion():
    global motion_time
    motion_time = time.time()
    return {"status": "motion_received"}

@app.route('/proximity', methods=['POST'])
def proximity():
    global proximity_time
    proximity_time = time.time()
    return {"status": "proximity_received"}

@app.route('/check', methods=['GET'])
def check():
    current_time = time.time()
    motion_valid = motion_time and (current_time - motion_time <= 10)
    proximity_valid = proximity_time and (current_time - proximity_time <= 10)
    if motion_valid and proximity_valid:
        return {"unlock": True}
    return {"unlock": False}

if __name__ == '__main__':
    app.run(port=5000)
