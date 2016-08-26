import smtplib
from getpass import getpass
from models import *


class Email_sender:
    def __init__(self, subject, recipient):
        self.subject = subject
        self.recipient = recipient
        self.body = Datas.create_email_body()

    def send_it(self):
        sender = input("Please enter your email address: ")
        password = getpass()
        count = 0
        try:
            for b in self.body:
                msg = "\r\n".join(["From: {}".format(sender), "To: {}".format(self.recipient),
                                   "Subject: {}".format(self.subject), "{}".format(b)])
                try:
                    if msg:
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.ehlo()
                        server.starttls()
                        server.login(sender, password)
                        server.sendmail(sender, self.recipient, msg)
                        server.quit()
                        count += 1
                except:
                    print("An error occured, email not sent.")
        finally:
            print("{} email(s) successfully sent to {}.".format(count, self.recipient))


class Datas:
    def __init__(self, first_name, last_name, application_code, school, status):
        self.first_name = first_name
        self.last_name = last_name
        self.application_code = application_code
        self.school = school
        self.status = status

    @staticmethod
    def get_data():
        email_list = []
        applicants = list(Applicant.select())
        for a in applicants:
            email_list.append(Datas(a.first_name, a.last_name, a.application_code, a.school.location, a.status))
        return email_list

    @staticmethod
    def create_email_body():
        bodies = []
        for person in Datas.get_data():
            body = "Hi {} {}! Your application code is {} in Codecool {}, and your status is {}.".format(person.first_name,
                                                                                                         person.last_name, person.application_code, person.school, person.status)
            bodies.append(body)
        return bodies



test = Email_sender("testing", "atelon09@gmail.com")
test.send_it()