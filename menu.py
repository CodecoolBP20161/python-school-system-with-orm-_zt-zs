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


def sub_menu():
    global choice
    print('\nAdmin menu'
          '\nChoose one from the following menu options and press enter.\n'
          'If you wish to exit the program press q.\n'
          '1. New Applicant\n'
          '2. Assign school to applicant    ')
    choice = input()
    return choice
if main_menu() == '1':
    if sub_menu() == '1':
        Applicant.create(first_name=input('First name: '), last_name=input('Last name: '), email=input('E-mail: '),
                             city=input('City: '))
    elif choice == '2':
        Applicant.update_school()
        print("Schools assigned to applicants.")
    elif sub_menu() == 'q':
        pass
    elif sub_menu() == 'b':
        main_menu()
    else:
        sub_menu()
elif main_menu() == 'q':
    pass
else:
    main_menu()