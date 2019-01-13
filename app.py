from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hellow'

@app.route('/json-example', methods=['POST'])
def json_example():
    req_data = request.form
    print(req_data)
    name = req_data['name']
    return '''The name value is: {}'''.format(name)

if __name__ == "__main__":
    app.run()