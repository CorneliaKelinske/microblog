from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cornelia'}
    posts = [
        {
            'author': {'username': 'Gary'},
            'body': 'Another Day at the Lake'

        },

        {
            'author': {'username': 'Julia'},
            'body': 'Down to One Gear'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
