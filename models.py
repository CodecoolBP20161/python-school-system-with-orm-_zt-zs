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

    @staticmethod
    def ask_details():
        your_app_code = input("Please enter your application code: ")
        query = Applicant.select().where(Applicant.application_code == your_app_code)
        if query:
            for i in query:
                s = School.get(School.id == i.school)
                school = School.select().join(Applicant, on=(School.id == s)).get()
                print("Hello", i.first_name, i.last_name + "!", "Your status is", "'" + i.status + "'" ,
                      "in Codecool", school.location + ".")
        else:
            print("No such application code.")

    @staticmethod
    def interview_details():
        your_app_code = input("Please enter your application code: ")
        query = Applicant.select().where(Applicant.application_code == your_app_code)
        if query:
            for i in query:
                s = School.get(School.id == i.school)
                school = School.select().join(Applicant, on=(School.id == s)).get()
                print("Hello", i.first_name, i.last_name + "!", "Your status is", "'" + i.status + "'" ,
                      "in Codecool", school.location + ".")
        else:
            print("No such application code.")

    @staticmethod
    def filter_applicants(filterby):
        print("\nFilter by", filterby)

        if filterby == "school":
            schools = [("Budapest press 1,"), ("Miskolc 2,"), ("Krakow 3")]
            print("For Codecool", end="")
            for school in schools:
                print(" {0}".format(school), end="")

        if filterby == "interview":
            interview_slots = InterviewSlot.select().where(InterviewSlot.status == False)
            print("Reserved interview slots (enter interview id number):")
            for i in interview_slots:
                print(i.id, i.date)

        if filterby == "mentor":
            mentors = Mentor.select().where(Mentor.id > 0)
            print("Mentors (enter mentor id number):")
            for i in mentors:
                print(i.id, i.first_name, i.last_name)

        exact_filter = input("\nPlease enter your parameter: \n")
        try:
            connect = getattr(Applicant, filterby)
            if connect:
                connect_school = getattr(School, "location")
                query_school = School.select().where(connect_school == exact_filter)

                for f in query_school:
                    print("Codecool", f.location)

                query = Applicant.select().where(connect == exact_filter)
                for i in query:
                    if filterby == "school":
                        s = School.get(School.id == i.school)
                        school = School.select().join(Applicant, on=(School.id == s)).get()
                        print("{} {}, {}: {}".format(i.first_name, i.last_name, filterby, school.location))

                    elif filterby == "interview":
                        e = InterviewSlot.get(InterviewSlot.id == i.interview)
                        interview = Interview.select().join(Applicant, on=(Interview.details == e)).get()
                        connect = InterviewSlot.get(InterviewSlot.id == interview.details)
                        date = InterviewSlot.get(InterviewSlot.id == connect.id)

                        if date.date:
                            print("{} {}, {}: {}".format(i.first_name, i.last_name, filterby, date.date))
                        else:
                            print("No interview date yet.")
                    elif filterby == "mentor":
                        e = InterviewSlot.get(InterviewSlot.id == i.interview)
                        interview = Interview.select().join(Applicant, on=(Interview.details == e)).get()
                        connect = InterviewSlot.get(InterviewSlot.id == interview.details)
                        mentor = InterviewSlot.get(InterviewSlot.mentor == Mentor.id)
                        print("{} {}, {}: {}".format(i.first_name, i.last_name, filterby, mentor.first_name, mentor.last_name))

                    else:
                        print("{} {}, {}: {}".format(i.first_name, i.last_name, filterby, exact_filter))
        except:
            if filterby == "mentor":
                connect = getattr(Mentor, "id")
                query_mentor = Mentor.select().where(connect == exact_filter)
                for m in query_mentor:
                    date = InterviewSlot.get(InterviewSlot.mentor == m.id)
                    applicant = Applicant.select().join(Interview, on=(Interview.applicant == Applicant.id)).get()
                    print("{} {}, {} {} {}".format(m.first_name, m.last_name, date.date, applicant.first_name, applicant.last_name))


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
                connected_city = School.get(School.id == applicant.school)
                if date.school == connected_city:
                    free_slots.remove(date)
                    Interview.create(applicant=applicant, details=date)
                    applicant.status = "In progress"
                    applicant.interview = date
                    date.status = False
                    applicant.save()
                    date.save()
                    no_interview.remove(applicant)
                    break


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant)
    details = ForeignKeyField(InterviewSlot)


class Question(BaseModel):
    pass


class Answer(BaseModel):
    pass
