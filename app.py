from flask import *
from models import *
import requests
import sys

TEMPLATE_REGISTRATION = 'registration.html'

DEBUG = False

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


@app.route('/registration_route', methods=['GET'])
def registrate_begin():
    cities_to_display = get_cities()
    return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display)


def get_cities():
    cities_to_display = []
    for city in City.select():
        cities_to_display.append(city.all_cities)
    return set(sorted(cities_to_display))


@app.route('/registration_route', methods=['POST'])
def validate_registration():
    cities_to_display = get_cities()
    if (request.method == 'POST' and request.form["first_name"] and request.form["last_name"] and
            request.form["email"] and request.form["city"]):
        try:
            Applicant.create(first_name=request.form["first_name"], last_name=request.form["last_name"],
                             email=request.form["email"], city=request.form["city"])

        except IntegrityError:
            email_exists_error = True
            return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display, email="Enter another email address",
                                   first_name=request.form["first_name"], last_name=request.form["last_name"],
                                   city=request.form["city"], email_exists_error=email_exists_error)
    else:
        first_name_missing, last_name_missing, email_missing, city_missing = False, False, False, False
        if not request.form["first_name"]:
            first_name_missing = True
        if not request.form["last_name"]:
            last_name_missing = True
        if not request.form["email"]:
            email_missing = True
        if not request.form["city"]:
            city_missing = True
        return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display, email=request.form["email"],
                               first_name=request.form["first_name"], last_name=request.form["last_name"],
                               city=request.form["city"], first_name_missing=first_name_missing,
                               last_name_missing=last_name_missing, email_missing=email_missing,
                               city_missing=city_missing)
    return redirect('/')


@app.route('/info', methods=['GET'])
def display_infos():
    return render_template("info.html")


@app.route('/contact', methods=['GET'])
def contacting():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
