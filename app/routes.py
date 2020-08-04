from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/connie')
def connie():
    return "Hello Connie"