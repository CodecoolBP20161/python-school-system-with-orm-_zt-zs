from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
# generating local connect string into a txt file


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


db = PostgresqlDatabase(connect_list()[0], user=connect_list()[1])


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
