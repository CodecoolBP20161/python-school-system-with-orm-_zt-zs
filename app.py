from flask import *
from models import *
import requests


DEBUG = True

app = Flask(__name__, static_folder='images')
app.config.from_object(__name__)



@app.before_request
def before_request():
    g.database = db
    g.database.connect()


@app.after_request
def after_request(response):
    g.database.close()
    return response


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/registration_route', methods=['GET', 'POST'])
def registrate():
    cities_to_display = []
    for city in City.select():
        cities_to_display.append(city.all_cities)
    if (request.method == 'POST' and request.form["first_name"] and request.form["last_name"] and
        request.form["email"] and request.form["city"]):
        Applicant.create(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            city=request.form["city"])
        return redirect('/')
    else:
        return render_template('registration.html', cities=cities_to_display)


if __name__ == '__main__':
    app.run()
