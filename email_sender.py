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

    def send_it(self):
        data = self.get_applicant_data()
        # sender = input("Please enter your email address: ")
        sender = "atelon09@gmail.com"
        # password = getpass()
        password = "10qwert01"
        count = 0

        you = "atelon09@gmail.com"


        try:
            for d in data:
                html = """\
                <html>
                    <head>
                        <title>GTFO!</title>
                    </head>
                    <body>
                        <img src="https://github.com/CodecoolBP20161/python-school-system-with-orm-_zt-zs/blob/email_html/static/cc_logo-large.png?raw=true">
                        <p>Hey u peace of shit loser {} {} !</p>
                        <br>
                        <p>How did u even got the idea to apply to the mighty Codecool {} ?? Were u out of ur stupid mind?</p>
                        <p>Ur status is obv '{}' . Forget about ur ridiculous name, from now on ur called {}.</p>
                        <p>Get ur shit together, and if u can find some courage in ur meaningless self for once in ur pathetic life,</p>
                        <p>and if for some unthinkable reason we decide u worth it were gonna send u an interview date later, so u can</p>
                        <p>show us ur ugly face at Codecool {} .</p><br>
                        <br>
                        <p>Until then, continue to waste our precious air for the last time,</p>
                        <p>Trainers at Codecool {}</p>
                    </body>
                </html>
                """.format(d[0][0], d[0][1], d[0][2], d[0][4], d[0][3], d[0][2], d[0][2])

                part2 = MIMEText(html, 'html')
                # msg = "\r\n".join(["From: {}".format(sender), "To: {}".format(self.recipient),
                #                        "Subject: {}".format(self.subject), "{}".format(html)])
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Your Application"
                msg['From'] = sender
                msg['To'] = you
                if msg:
                    msg.attach(part2)
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(sender, password)
                    server.sendmail(sender, you, msg.as_string())
                    server.quit()
                    count += 1

        finally:
            print("{} email(s) successfully sent.".format(count))


test.send_it()