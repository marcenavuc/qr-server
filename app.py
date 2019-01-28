from flask import Flask, render_template, request, redirect, session
import json
import psycopg2

app = Flask(__name__)
app.secret_key = "mashine_learning"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')
    if name == 'blokchain':
        session['logged_in'] = True
        return redirect('/table')
    else:
        return render_template('index/index.html')

@app.route('/table', methods=['GET', 'POST'])
def table():
    if not session.get('logged_in'):
        return redirect('/')
    else:
        try:
            connection = psycopg2.connect(user="mnaoikjnojorsv",
                                          password="dd47b86a853ec65e1a76a003a07d717ecfc20af547721d750042bafdfbf37520",
                                          host="ec2-54-75-245-94.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="df87fg6nok0dv8")
            cursor = connection.cursor()
            cursor.execute("SELECT * from release")
            connection.commit()
            response = cursor.fetchall()
            return render_template('table/table.html', data=sorted(response))
        except (Exception, psycopg2.Error) as error:
            print(error)
            return '''Error while loading data. Sorry :('''

@app.route('/json-api', methods=['POST'])
def json_example():
    req_data = request.get_json()
    id = req_data['id']
    print(json.dumps({'id': id}))
    insert_data = '''SELECT visited from release WHERE id = {};'''.format(id)
    try:
        connection = psycopg2.connect(user="mnaoikjnojorsv",
                                      password="dd47b86a853ec65e1a76a003a07d717ecfc20af547721d750042bafdfbf37520",
                                      host="ec2-54-75-245-94.eu-west-1.compute.amazonaws.com",
                                      port="5432",
                                      database="df87fg6nok0dv8")
        cursor = connection.cursor()
        cursor.execute(insert_data)
        connection.commit()
        response = cursor.fetchall()
        cursor.execute('''UPDATE release SET visited = true WHERE id = {};'''.format(id))
        connection.commit()
        print(response, response[0], id)
        visited = response[0]
        if id <= 246:
            row = (id // 25) + 1
            place = id % 25
        else:
            row = 11
            place = id - 246
        return json.dumps({
            "row": row,
            "place": place,
            "visited": visited
        })
    except (Exception, psycopg2.Error) as error:
        print(error)
        return json.dumps({"name": "err"})

@app.route('/wake-up')
def wake_up():
    return 'OK'

if __name__ == "__main__":
    app.run()