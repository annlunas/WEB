from app import app
from flask import render_template, url_for


@app.route('/')
@app.route('/hello')
def hello():
    return render_template('index.html')


@app.route('/users2/<username>')
def users2(username):
    return 'User %s' % username


@app.route('/users/<username>')
def users(username):
    return render_template('index2.html')


with app.test_request_context():
    print(url_for('hello'))
    print(url_for('users', username='PeppaPig'))
