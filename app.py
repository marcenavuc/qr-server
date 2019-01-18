from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'v: 1.0.0'

@app.route('/json-example', methods=['POST'])
def json_example():
    print(request.form)
    req_data = request.form
    print(req_data)
    name = req_data['id']
    return ''.format(name)

@app.route('/wake-up')
def wake_up():
    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run()