# This script can generate example data for "City" and "InterviewSlot" models.

from models import *



City.delete()
School.delete()
Applicant.delete()

codecool_bp = School.create(location = "Budapest")
codecool_miskolc = School.create(location = "Miskolc")
codecool_krakow = School.create(location = "Kraków")

miskolc = City.create(all_cities="Miskolc", cc_cities="Miskolc")
budapest = City.create(all_cities="Budapest", cc_cities="Budapest")
pecs = City.create(all_cities="Pécs", cc_cities="Budapest")
szeged = City.create(all_cities="Szeged", cc_cities="Budapest")
debrecen = City.create(all_cities="Debrecen", cc_cities="Miskolc")
szfehervar = City.create(all_cities="Székesfehérvár", cc_cities="Budapest")
nyegyhaza = City.create(all_cities="Nyíregyháza", cc_cities="Miskolc")
eger = City.create(all_cities="Eger", cc_cities="Miskolc")
satoraljaujhely = City.create(all_cities="Sátoraljaújhely", cc_cities="Miskolc")
gyor = City.create(all_cities="Győr", cc_cities="Budapest")
krakow = City.create(all_cities="Kraków", cc_cities="Kraków")
warsaw = City.create(all_cities="Warsaw", cc_cities="Warsaw")

kovacsbela = Applicant.create(first_name="Béla", last_name="Kovács", email="belakovacs@gmail.com", city="Budapest")
kovacsanna = Applicant.create(first_name="Anna", last_name="Kovács", email="annak_ovacs@gmail.com", city="Miskolc")
kissistvan = Applicant.create(first_name="István", last_name="Kiss", email="istvankiss01@gmail.com", city="Eger")
nagynora = Applicant.create(first_name="Nóra", last_name="Nagy", email="nagynorann@gmail.com", city="Pécs")
matheuszzcyl = Applicant.create(first_name="Matheusz", last_name="Zcyl", email="zmatheusz@gmail.com", city="Kraków")
tothlaszlo = Applicant.create(first_name="László", last_name="Tóth", email="laci90@gmail.com",  city="Szeged")
johndoe = Applicant.create(first_name="John", last_name="Doe", email="thisismyemail@gmail.com", city="Warsaw")


print(kovacsbela.email)