# This script can create the database tables based on your models

from models import *


db.connect()
# Delete existing tables to avoid conflicts
db.drop_tables([Applicant, School, City, Mentor, InterviewSlot,
                  Interview, Question, Answer], safe=True)
# List the tables here what you want to create...
db.create_tables([Applicant, School, City, Mentor, InterviewSlot,
                  Interview, Question, Answer], safe=True)
