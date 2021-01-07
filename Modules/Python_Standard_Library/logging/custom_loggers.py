import logging as log

#______workuing with loggers_________#
# Creating logger
logger = log.getLogger(__name__)
# setting logger level
logger.setLevel(log.INFO)
# Creating a Formatter object
formatter = log.Formatter('%(levelname)s: %(name)s: %(message)s')

#________Creating a file handler__________#
file_path = __file__.replace('custom_loggers.py', 'employee.log')
# A handler class which writes formatted logging records to log files.
file_handler = log.FileHandler(file_path)
file_handler.setFormatter(formatter)

# Giving our custom logger a Filehandler object
logger.addHandler(file_handler)

class Employee():

    def __init__(self, first: str, last: str):
        self.firstname = first
        self.lastname = last
        """After you create a custom logger do not forget to use the identifier
        of that logger insted of the module name"""
        logger.info(f"Created employee: {self.fullname()} - {self.email()}")

    def email(self):
        return f"{self.firstname}.{self.lastname}@email.com"

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

emp1 = Employee('Ken', 'Rosenberg')
emp2 = Employee('Tommy', 'Vercetti')
emp3 = Employee('Avery', 'Carrington')