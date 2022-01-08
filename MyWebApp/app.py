import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)



conn = psycopg2.connect(dbname='flask_db', user='postgres',
                        password='123456', host='localhost')

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    cur = conn.cursor()
    username = request.form.get('username')
    password = request.form.get('password')
    cur.execute("SELECT * FROM users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cur.fetchall())


    if not username:
        not_field = 'Поле "Username" не заполнено, попробуйте ещё раз.'
        return render_template('login.html', not_field=not_field)
    if not password:
        not_field = 'Поле "Password" не заполнено, попробуйте ещё раз.'
        return render_template('login.html', not_field=not_field)

    # пользователя не существует
    if not records:
        return render_template('error_form.html')
    else:
        return render_template('account.html', full_name=records[0][1], lgn=username, psswrd=password)


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        cur.execute('INSERT INTO users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()

        return redirect('/login/')

    return render_template('registration.html')

