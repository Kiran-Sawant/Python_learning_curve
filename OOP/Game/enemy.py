"""Inheritance(line 30), Method overriding(line 54)"""

import random

class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):      #__str__ is executed with the class instance without the need for calling
        return 'Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}'.format(self)

#_____Making a subclass_____#
class Troll(Enemy):         #The class Troll inherits from its superclass Enemy
    
    def __init__(self, name):
        # super(Troll, self).__init__(name=name,  hit_points=23, lives= 1)      #inheriting __init__ of super class
        super().__init__(name=name, hit_points=26, lives=1)                     #same as line 33

    def grunt(self):        #A property of troll class or an attribute of an instance of troll class
        print('Me {0.name}, {0.name} Stomp you!!!'.format(self))

#_____Making a subclass_____#
class Vampyre(Enemy):       #The class Vampyre inherits from class Enemy

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    #_______Creating a method_______#
    def dodge(self):
        if random.randint(1, 3) == 3:
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    #________Overriding the take_damage method__________#
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)      #calling a method of the super class

#_____Making a supersubclass_____#
class VampyreKing(Vampyre):
    """The class Vampyre inherits from class Enemy,
    the class VampyreKing is a supersub class of Enemy class.
    VampyreKing class overrides the method mentioned in its super-class
    which overrides the method in Enemy class."""

    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 140

    # Method overriding
    def take_damage(self, damage):
        super().take_damage(damage // 4)
        """super() is a proxy method that gives access to super classes methods and attributes.
        It can be very useful when inheriting from multiple classes."""