from flask import *
from models import *
import requests
import sys



TEMPLATE_REGISTRATION = 'registration.html'
SECRET_KEY = "cafebabe"
app.secret_key = SECRET_KEY

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
    # print('registrate begin', file=sys.stderr)
    # session["new_applicant"] = Applicant(first_name="", last_name="", city="", email="")
    cities_to_display = get_cities()
    return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display)


def get_cities():
    cities_to_display = []
    for city in City.select():
        cities_to_display.append(city.all_cities)
    return sorted(cities_to_display)


@app.route('/registration_route', methods=['POST'])
def validate_registration():

    cities_to_display = get_cities()
    # print('validate_registration new_applicant=%s' % (str(session.get("new_applicant"))), file=sys.stderr)
    if (request.method == 'POST' and request.form["first_name"] and request.form["last_name"] and
            request.form["email"] and request.form["city"]):
        try:
            Applicant.create(
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                email=request.form["email"],
                city=request.form["city"])
            return redirect('/')
        except IntegrityError:
            return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display, error_message="existing email",
                                   first_name=request.form["first_name"], last_name=request.form["last_name"], city =
            request.form["city"])


if __name__ == '__main__':
    app.run()
