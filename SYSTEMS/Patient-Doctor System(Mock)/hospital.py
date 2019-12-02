'''
System Flow
'''
import patient
import doctor

print('CARLTON HOSPITAL')
# List of in-house doctors
doc_on_call = ['DAVID', 'AARON', 'VICTOR', 'HARRY', 'ASHLEY',
               'FRED', 'SCOTT', 'PAUL', 'DANIEL', 'MARCUS', 'ANTHONY']
# List of previous patients
previous_patients = ['GEA', 'BISSAKA', 'LINDELOF', 'MAGUIRE', 'YOUNG',
                     'FRED', 'MCTOMINAY', 'POGBA', 'JAMES',
                     'RASHFORD', 'MARTIAL']

visitor = input('Are you a patient or a doctor? (P or D): ')
if visitor[0].lower() == 'p':

    while True:

        try:
            print('Please enter your details')
            p_name = input('What is your name? ')
            p_age = int(input('How old are you? '))
            p_height = int(input('What is your height in CM? '))
            p_weight = int(input('What is your weight in KG? '))

        except ValueError:
            print('Invalid entry. Please try again')

        else:
            if p_name.upper() in previous_patients:
                print('Welcome back to CARLTON HOSPITAL')
                pat = patient.Patient(p_name, p_age, p_height, p_weight)
                print(pat)
                print('We have your history {}'.format(pat.history))
            else:
                print('Welcome to CARLTON HOSPITAL.')
                pat = patient.Patient(p_name, p_age, p_height, p_weight)
                print(pat)
                print('This is your first time here')
            break

elif visitor[0].lower() == 'd':

    while True:
        vis_id = input('What is your name? ')
        if vis_id.upper() in doc_on_call:
            doctor.Doctor(vis_id)
            print('Welcome back doctor')
            break
        else:
            print('You are not a doctor in CARLTON HOSPITAL')
        break

else:
    print('We only help patients and doctors')

# Doctors office
nurse_request = input('Doctor should we send the patients in? (Y or N) ')
if nurse_request[0].lower() == 'y':
    print('Okay, Let me send them in one by one')
    doctor.Doctor('JAMES').patients.append(pat)
    doctor.Doctor('POGBA').patients.append(pat)
    doctor.Doctor('RASHFORD').patients.append(pat)
    doctor.Doctor('GEA').show_patients()
elif nurse_request[0].lower() == 'n':
    print('Okay Doc. You need your time')
else:
    print('The doctor is not seeing anyone')
