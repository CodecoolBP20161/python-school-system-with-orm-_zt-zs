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
            error_message = "email already exists"
            return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display, email=error_message,
                                   first_name=request.form["first_name"], last_name=request.form["last_name"],
                                   city=request.form["city"])
    else:
        error = True
        return render_template(TEMPLATE_REGISTRATION, cities=cities_to_display, email=request.form["email"],
                               first_name=request.form["first_name"], last_name=request.form["last_name"],
                               city=request.form["city"], error=error)
    return redirect('/')


@app.route('/info', methods=['GET'])
def display_infos():
    return render_template("info.html")


@app.route('/mentor/login', methods=['GET', 'POST'])
def mentor_login():
    mentors = Mentor.select()
    error = None
    if request.method == 'POST':
        for mentor in mentors:
            if request.form['email'] != mentor.email:
                error = 'Invalid username'
            elif request.form['pwd'] != mentor.password:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('/'))

    return render_template('login.html', error=error)


from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# @login_required
@app.route('/test', methods=['GET', 'POST'])
def test_login():
    mentors = Mentor.select().get()
    logged_in = True
    return render_template("test.html", logged_in='logged_in', mentor="mentors")


@app.route('/contact', methods=['GET'])
def contacting():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=5001)
