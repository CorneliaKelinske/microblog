from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Connie'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

