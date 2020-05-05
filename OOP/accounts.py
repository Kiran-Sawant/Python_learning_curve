"""static methods, mangled instance attributes, hidden variables"""

import datetime as dt
import pytz


class Account:
    """Creates a simple account with balance
    
    Attributes:
        name (str): Name of account holder
        balance (float): Deposit at opening"""

    #________Creating static methods________#
    @staticmethod
    def _current_time():
        '''static methods are only used inside a class and start with a underscore conventionally
       they can be used outside classes as well but doing so is not adviced'''
        utc_time = dt.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, _name, __balance): #__balance is a mangled attribute
        self._name = _name                #attribute names starting with double underscore are mangled
        self.__balance = __balance        #__balaance is mangled with class name ie. _Account__balance
        self.transaction_list = []
        self.transaction_list.append((Account._current_time(), __balance))
        print("\nAccount created for {0._name}".format(self))

    def deposit(self, amount):
        '''Credit funds into account
        
        Attributes:
            amount (float): The amount of fund to deposit'''

        if amount > 0:
            self.__balance += amount
            Account.show_balance(self)
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        '''Debits funds from the account
        
        Attributes:
            amount (float): The amount of funds to withdraw'''

        if amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print('Invalid amount!, max withdrawal ${0.__balance} only'.format(self))

    def show_balance(self):
        '''Displays the leftover balance in the Bank account'''

        print('Your balance is {}'.format(self.__balance))

    def show_transactions(self):
        '''Displays all the transaction history'''

        print('\nTransaction list:-')
        for date, amount in self.transaction_list:
            if amount > 0:
                type_ = 'Credit'
            else:
                type_ = 'Debit'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, type_, date, date.astimezone()))

if __name__ == "__main__":
    kiran = Account('Kiran', 0)
    kiran.deposit(1000)
    kiran.withdraw(500)
    kiran.withdraw(100)
    kiran.withdraw(50)
    # kiran.withdraw(600)
    kiran.show_transactions()

    steph = Account('steph', 800)
    steph.deposit(500)
    steph.withdraw(200)
    steph.show_transactions()