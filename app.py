from flask import *


debug = True

app = Flask(__name__, static_folder='images')
app.config.from_object(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/registration_route')
def registrate():
    return 'Registration form goes here'


if __name__ == '__main__':
    app.run()