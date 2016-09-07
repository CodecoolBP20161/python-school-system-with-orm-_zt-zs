from models import *
from email_sender import *


class Menu:

    def __init__(self, menu_options, menu_actions):
        self.menu_options = menu_options
        self.menu_actions = menu_actions

    def print_menu(self):
        for option in enumerate(self.menu_options):
            print('{}. {}'.format(option[0] + 1, option[1]))
        Menu.menu_action(self)

    def menu_action(self):
        choice = int(input('Enter the number of the menu option you wanna perform: '))
        for option in enumerate(self.menu_options):
            if option[0] + 1 == choice:
                for function in self.menu_actions[choice - 1]:
                    exec(function)


mentor_menu = Menu(
    ['Interview details'],
    [['Mentor.ask_name()']]
)

applicant_menu = Menu(
    ['Application details', 'Interview details'],
    [['Applicant.application_details()'], ['Applicant.interview_details()']]
)

applicant_filters = Menu(
    ['status', 'time', 'location', 'first name', 'last name', 'email', 'school', 'assigned mentor'],
    [['Applicant.filter_applicants("status")'],
     ['Applicant.filter_applicants("interview")'],
     ['Applicant.filter_applicants("city")'],
     ['Applicant.filter_applicants("first_name")'],
     ['Applicant.filter_applicants("last_name")'],
     ['Applicant.filter_applicants("email")'],
     ['Applicant.filter_applicants("school")'],
     ['Applicant.filter_applicants("mentor")']]
)

admin_menu = Menu(
    ['Assign school and application code to applicant(s), send email about it', 'Assign interview to applicant(s) with application code',
     'Get applications details by filter'],
    [['Applicant.update_school()', 'Applicant.detect()',
      'print("School and application code assigned to applicant(s).")', 'Email_sender.send_it()'],
     ['InterviewSlot.give_interview()',
      '''print("Interview date assigned to applicant(s). Status updated to 'In progress'.")'''],
     ['applicant_filters.print_menu()']]
)

main_menu = Menu(
    ['Admin', 'Applicant', 'Mentor'],
    [['admin_menu.print_menu()'], ['applicant_menu.print_menu()'], ['mentor_menu.print_menu()']]
)

main_menu.print_menu()
