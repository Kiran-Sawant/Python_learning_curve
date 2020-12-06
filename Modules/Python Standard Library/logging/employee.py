"""This script contains a Employee class that logs the full name and email address
of the employee everytime an employee object is created."""

import logging as log

path = r"D:\my_space\software_projects\Python\Learning_curve\Modules\Python Standard Library\logging"
log.basicConfig(level=log.DEBUG, filename=path + r'\employee.log',
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

emp1 = Employee('Ken', 'Rosenberg')
emp2 = Employee('Tommy', 'Vercetti')
emp3 = Employee('Avery', 'Carrington')
