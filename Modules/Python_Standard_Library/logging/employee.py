"""This script contains a Employee class that logs the full name and email address
of the employee everytime an employee object is created."""

import logging as log

path = __file__.replace('employee.py', 'employee.log')
log.basicConfig(level=log.DEBUG, filename=path,
                format='%(levelname)s: %(name)s : %(message)s')

class Employee():

    def __init__(self, first: str, last: str):
        self.firstname = first
        self.lastname = last
        # log call
        log.info(f"Created employee: {self.fullname()} - {self.email()}")

    def email(self):
        return f"{self.firstname}.{self.lastname}@email.com"

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

# Creating Employee instances
emp1 = Employee('Ken', 'Rosenberg')
emp2 = Employee('Tommy', 'Vercetti')
emp3 = Employee('Avery', 'Carrington')
