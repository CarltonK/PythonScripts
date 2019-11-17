'''
This module contains all relevant doctor information
'''

class Doctor():

    def __init__(self, doc_name, patients=[]):
        self.doc_name = doc_name
        self.patients = patients

    def show_patients(self):
        for entry in self.patients:
            print(entry)

    def __str__(self):
        return 'NAME: {}\nPATIENTS: {}'.format(self.doc_name, self.schedule)
