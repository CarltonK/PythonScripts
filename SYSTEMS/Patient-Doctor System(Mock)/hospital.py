'''
System Flow
'''
import patient
import doctor

print('CARLTON HOSPITAL')
visitor = input('Are you a patient or a doctor? (P or D): ')
if visitor[0].lower() == 'p':
    try:
        p_name = input('What is your name? ')
        p_age = int(input('How old are you? '))
        p_height = int(input('What is your height in CM? '))
        p_weight = int(input('What is your weight in KG? '))

    except ValueError:
        print('Invalid entry. Please try again')

    else:
        pat = patient.Patient(p_name, p_age, p_height, p_weight)
        print(pat)
elif visitor[0].lower() == 'd':
    pass
else:
    print('We only help patients and doctors')
