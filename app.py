from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return 'v: 1.0.0'

@app.route('/json-example', methods=['POST'])
def json_example():
    print(request.get_json())
    req_data = request.get_json()
    name = req_data['id']
    print(json.dumps({'id': name}))
    return json.dumps({'id': name})

@app.route('/wake-up')
def wake_up():
    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run()