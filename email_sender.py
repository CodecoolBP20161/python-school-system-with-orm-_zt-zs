import smtplib
from getpass import getpass
from models import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email_sender:
    def __init__(self, subject, recipient):
        self.subject = subject
        self.recipient = recipient

    @staticmethod
    def get_applicant_data():
        new_applicants = list(Applicant.select().where(Applicant.status == "New"))
        applicant_datas = []
        for applicant in new_applicants:
            applicant_datas.append(([applicant.first_name, applicant.last_name, applicant.school.location,
                                     applicant.application_code, applicant.status], applicant.email))
        return applicant_datas


    @classmethod
    def application_body(cls, applicant):
        try:
            cls.subject = "Your Application"
            html_template = """\
                <html>
                    <head>
                        <title>GTFO!</title>
                    </head>
                    <body style="text-align: justify;">
                        <img src="https://github.com/CodecoolBP20161/python-school-system-with-orm-_zt-zs/blob/email_html/static/cc_logo-large.png?raw=true">
                        <p>Hey u peace of shit loser <strong>{} {}</strong> !</p>
                        <br>
                        <p>How did u even got the idea to apply to the mighty <strong>Codecool {}</strong>?? Were u out of ur stupid mind?</p>
                        <p>Ur status is obv '<strong>{}</strong>' . Forget about ur ridiculous name, from now on ur called <strong>{}</strong>.</p>
                        <p>Get ur shit together, and if u can find some courage in ur meaningless self for once in ur pathetic life,</p>
                        <p>and if for some unthinkable reason we decide u worth it were gonna send u an interview date later, so u can</p>
                        <p>show us ur ugly face at <strong>Codecool {}</strong>.</p><br>
                        <br>
                        <p>Until then, continue to waste our precious air for the last time,</p>
                        <p>Trainers at <strong>Codecool {}</strong></p>
                    </body>
                </html>
                """.format(applicant[0][0], applicant[0][1], applicant[0][2], applicant[0][4], applicant[0][3],
                           applicant[0][2], applicant[0][2])
            html_body = MIMEText(html_template, 'html')
            return html_body
        except:
            pass

    @classmethod
    def send_it(cls, data, subject):
        cls.subject = subject
        count = 0
        try:
            for applicant in data:

                # hard coded sender infos
                sender = "atelon09@gmail.com"
                password = "10qwert01"

                # # arbitrary sender infos
                # sender = input("Please enter your email address: ")
                # password = getpass()

                cls.recipient = "atelon09+{}@gmail.com".format(applicant[1])
                msg = MIMEMultipart()
                msg['Subject'] = cls.subject
                msg['From'] = sender
                msg['To'] = cls.recipient

                html_body = cls.application_body(applicant)

                sender = "atelon09@gmail.com"
                password = "10qwert01"

                cls.recipient = "atelon09@gmail.com"
                try:
                    if msg:
                        msg.attach(html_body)
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.ehlo()
                        server.starttls()
                        server.login(sender, password)
                        server.sendmail(sender, cls.recipient, msg.as_string())
                        server.quit()
                        count += 1
                except:
                    print("An error occured.")
        finally:
            print("{} email(s) successfully sent.".format(count))
