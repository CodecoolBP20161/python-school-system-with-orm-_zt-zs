# This script can generate example data for "City" and "InterviewSlot" models.

from models import *


codecool_bp = School.create(location="Budapest")
codecool_miskolc = School.create(location="Miskolc")
codecool_krakow = School.create(location="Krakow")


miskolc = City.create(all_cities="Miskolc", cc_cities=codecool_miskolc)
budapest = City.create(all_cities="Budapest", cc_cities=codecool_bp)
pecs = City.create(all_cities="Pécs", cc_cities=codecool_bp)
szeged = City.create(all_cities="Szeged", cc_cities=codecool_bp)
debrecen = City.create(all_cities="Debrecen", cc_cities=codecool_miskolc)
szfehervar = City.create(all_cities="Székesfehérvár", cc_cities=codecool_bp)
nyegyhaza = City.create(all_cities="Nyíregyháza", cc_cities=codecool_miskolc)
eger = City.create(all_cities="Eger", cc_cities=codecool_miskolc)
satoraljaujhely = City.create(all_cities="Sátoraljaújhely", cc_cities=codecool_miskolc)
gyor = City.create(all_cities="Győr", cc_cities=codecool_bp)
krakow = City.create(all_cities="Krakow", cc_cities=codecool_krakow)
warsaw = City.create(all_cities="Warsaw", cc_cities=codecool_krakow)


kisattila = Applicant.create(first_name="Attila", last_name="Kiss", email="atelon09+kattila@gmail.com", city="Budapest")
jakabanna = Applicant.create(first_name="Anna", last_name="Jakab", email="atelon09+annak_j@gmail.com", city="Miskolc")
nagyemese = Applicant.create(first_name="Emese", last_name="Nagy", email="atelon09+emesenagy01@gmail.com", city="Eger")
feketetibor = Applicant.create(first_name="Tibor", last_name="Fekete", email="atelon09+tibif@gmail.com", city="Pécs")
matheuszzcyl = Applicant.create(first_name="Matheusz", last_name="Zcyl", email="atelon09+zmatheusz@gmail.com", city="Krakow")
barnajanka = Applicant.create(first_name="Janka", last_name="Barna", email="atelon09+jankab90@gmail.com",  city="Szeged")
johndoe = Applicant.create(first_name="John", last_name="Doe", email="atelon09+thisismyemail@gmail.com", city="Warsaw")


miki = Mentor.create(first_name="Miki", last_name="Beöthy", school=codecool_bp)
dani = Mentor.create(first_name="Dani", last_name="Salamon", school=codecool_bp)
tomi = Mentor.create(first_name="Tomi", last_name="Tompa", school=codecool_bp)
matheusz = Mentor.create(first_name="Matheusz", last_name="Ostafil", school=codecool_krakow)
attila = Mentor.create(first_name="Attila", last_name="Molnár", school=codecool_miskolc)


bp_interview = InterviewSlot.create(school=codecool_bp, mentor=miki, date='2016-09-01 10:00')
bp_interview2 = InterviewSlot.create(school=codecool_bp, mentor=miki, date='2016-09-01 11:00')
bp_interview3 = InterviewSlot.create(school=codecool_bp, mentor=dani, date='2016-09-01 10:00')
bp_interview4 = InterviewSlot.create(school=codecool_bp, mentor=dani, date='2016-09-01 11:00')
bp_interview5 = InterviewSlot.create(school=codecool_bp, mentor=tomi, date='2016-09-01 11:00')
bp_interview6 = InterviewSlot.create(school=codecool_bp, mentor=tomi, date='2016-09-01 13:00')
bp_interview7 = InterviewSlot.create(school=codecool_bp, mentor=miki, date='2016-09-01 13:00')
bp_interview8 = InterviewSlot.create(school=codecool_bp, mentor=tomi, date='2016-09-02 10:00')
bp_interview9 = InterviewSlot.create(school=codecool_bp, mentor=miki, date='2016-09-02 10:00')
bp_interview10 = InterviewSlot.create(school=codecool_bp, mentor=dani, date='2016-09-03 10:00')
bp_interview11 = InterviewSlot.create(school=codecool_bp, mentor=tomi, date='2016-09-03 10:00')
miskolc_interview = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-01 10:00')
miskolc_interview2 = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-01 11:00')
miskolc_interview3 = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-01 13:00')
miskolc_interview4 = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-02 10:00')
miskolc_interview5 = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-03 14:00')
miskolc_interview6 = InterviewSlot.create(school=codecool_miskolc, mentor=attila, date='2016-09-04 11:00')
krakow_interview = InterviewSlot.create(school=codecool_krakow, mentor=matheusz, date='2016-09-01 10:00')
krakow_interview2 = InterviewSlot.create(school=codecool_krakow, mentor=matheusz, date='2016-09-01 11:00')
krakow_interview3 = InterviewSlot.create(school=codecool_krakow, mentor=matheusz, date='2016-09-02 10:00')
krakow_interview4 = InterviewSlot.create(school=codecool_krakow, mentor=matheusz, date='2016-09-03 14:00')
krakow_interview5 = InterviewSlot.create(school=codecool_krakow, mentor=matheusz, date='2016-09-04 15:00')
