from models import *

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


applicant_menu = Menu(
    ['Application details', 'Interview details'],
    [['Applicant.ask_details()'], ['Applicant.interview_details()']]
)

applicant_filters = Menu(
    ['filters'],
    [['print("results")']]
)

admin_menu = Menu(
    ['Assign school and application code to applicant(s)', 'Assign interview to applicant(s) with application code',
     'Get applications details by filter'],
    [['Applicant.update_school()', 'Applicant.detect()',
      'print("School and application code assigned to applicant(s).")'],
     ['InterviewSlot.give_interview()',
      '''print("Interview date assigned to applicant(s). Status updated to 'In progress'.")'''],
     ['applicant_filters.print_menu()']]
)

main_menu = Menu(
    ['Admin', 'Applicant', 'Mentor'],
    [['admin_menu.print_menu()'], ['applicant_menu.print_menu()'], ['print("Mentor menu under construction")']]
)

main_menu.print_menu()
