import smtplib
from getpass import getpass


class Email_sender:
    def __init__(self, subject, recipient, body):
        self.subject = subject
        self.recipient = recipient
        self.body = body

    def send_it(self):
        sender = input("Please enter your email address: ")
        password = getpass()
        msg = "\r\n".join(["From: {}".format(sender), "To: {}".format(self.recipient),
                           "Subject: {}".format(self.subject), "{}".format(self.body)])
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, self.recipient, msg)
            server.quit()
            print("Email successfully sent to {}.".format(self.recipient))
        except:
            print("An error occured, email not sent.")
