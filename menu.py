from models import *


choice = 0


def main_menu():
    global choice
    print('\nChoose one from the following menu options and press enter.\n'
          'If you wish to exit the program press q.\n\n'
          '1. Admin\n'
          '2. Applicant\n'
          '3. Mentor\n')
    choice = input()
    return choice


def admin_menu():
    global choice
    print('\nAdmin menu'
          '\nChoose one from the following menu options and press enter.\n'
          'If you wish to exit the program press q.\n'
          '1. New Applicant\n'
          '2. Assign school and application code to applicant(s)\n'
          '3. Assign interview to applicant(s) with application code\n')
    choice = input()
    return choice


def applicant_menu():
    global choice
    print('\nApplicant menu'
          '\nChoose one from the following menu options and press enter.\n'
          'If you wish to exit the program press q.\n'
          '1. Application details\n'
          '2. Interview details\n')
    choice = input()
    return choice

if main_menu() == '1':
    if admin_menu() == '1':
        Applicant.create(first_name=input('First name: '), last_name=input('Last name: '), email=input('E-mail: '),
                         city=input('City: '))
    elif choice == '2':
        Applicant.update_school()
        Applicant.detect()
        print("School and application code assigned to applicant(s).")
    elif choice == '3':
        InterviewSlot.give_interview()
        print("Interview date assigned to applicant(s). Status updated to 'In progress'.")
    elif admin_menu() == 'q':
        pass
elif main_menu() == '2':
    if applicant_menu() == '1':
        Applicant.ask_details()
    elif choice == '2':
        print("Interview details")
    elif admin_menu() == 'q':
        pass
elif main_menu() == 'q':
    pass
