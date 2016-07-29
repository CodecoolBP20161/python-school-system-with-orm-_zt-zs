from peewee import *
import random
import uuid


# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop


# write connection data to local file
def write_connect_data():
    with open('local_connect_data.txt', 'w') as connect_file:
        connect_file.write("{0}\n\
{1}".format(input("Please enter your dbname: "), input("Please enter your dbuser: ")))


# reading connection data from local file
def read_connect_data():
    with open('local_connect_data.txt', 'r') as connect_file:
        return connect_file.readlines()


# try whether local connection file exists
def connect_list():
    try:
        connect_data = read_connect_data()
    except Exception:
        write_connect_data()
        connect_data = read_connect_data()
    return connect_data


db = PostgresqlDatabase(connect_list()[0].strip(), user=connect_list()[1].strip())


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()
    # name = str('Codecool ' + location)


class City(BaseModel):
    all_cities = CharField()
    cc_cities = ForeignKeyField(School)





class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    city = CharField()
    status = CharField(default="New")
    interview = CharField(default=None, null=True)
    school = CharField(null=True)  # related_name="no_school"
    application_code = CharField(default=None, null=True, unique=True)

    @classmethod
    def update_school(cls):
        for i in cls.select().where(cls.school == None):
            i.school = City.get(City.all_cities == i.city).cc_cities
            i.save()

    def create_app_code(self, string_length=4):
        """Returns a random string of length string_length."""
        random = str(uuid.uuid4())  # Convert UUID format to a Python string.
        random = random.upper()  # Make all characters uppercase.
        random = random.replace("-", "")  # Remove the UUID '-'.
        self.application_code = random[0:string_length]  # Return the random string.
        # self.status = "In progress"
        self.save()

    @classmethod
    def detect(cls):
        no_app_code = cls.select().where(cls.application_code == None)
        for app_inst in no_app_code:
            app_inst.create_app_code()


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School)


class InterviewSlot(BaseModel):
    school = ForeignKeyField(School)
    mentor = ForeignKeyField(Mentor)
    date = DateTimeField()
    status = BooleanField(default=True)  # when the timeslot is available, status is True

    @classmethod
    def give_interview(cls):
        free_slots = list(cls.select().where(cls.status))
        no_interview = list(Applicant.select().where(Applicant.status == "New"))  # or Applicant.interview == None
        for date in free_slots:
            for applicant in no_interview:
                s = School.get(School.id == applicant.school)
                if date.school == s:  # date.status is True:  # and
                    Interview.create(applicant=applicant, details=date)
                    applicant.status = "In progress"
                    applicant.interview = date
                    date.status = False
                    applicant.save()
                    date.save()
                    # free_slots.remove(date)
                    # no_interview.remove(applicant)


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant)
    details = ForeignKeyField(InterviewSlot)


class Question(BaseModel):
    pass


class Answer(BaseModel):
    pass
