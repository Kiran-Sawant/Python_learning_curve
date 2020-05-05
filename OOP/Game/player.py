class Player(object):
    """creates a player object.
    
    Attributes:
        name (str): Name of the player"""

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
    #____________Getters and Setters_____________#
    """A getter method passes the value of the variable,
    A setter method sets the value of the variable to the passed argument.
    if a variable is not ment to be changed don't make a setter method for it
    if a variable is not ment to be displayed don't make a getter method for it"""
    #_____getters & setters for lives_____#
    def _get_lives(self):           #Getter for _lives
        return self._lives

    def _set_lives(self, lives):    #Setter for _lives
        if lives >= 0:
            self._lives = lives
        else:
            print('lives cannot be negative')
            self._lives = 0
    #_____getters & setters for level_____#
    def _get_level(self):           #Getter for _level
        return self._level

    def _set_level(self, level):    #setter for _level
        if level >=1:
            self._level += level
            self._score += (level*1000)
        elif (self._level + level) >= 1:
            self._level += level
            self._score += (level*1000)
        else:
            print('level cannot be less than 1')
            self._level = 1

    lives = property(_get_lives, _set_lives) #in property getter is entered first and then setter
    level = property(_get_level, _set_level) #if only a setter is mentioned the attribute becomes write only
                                             #if only a getter is mentioned the attribute becomes read only

    #_____getters & setters using decorators______#

    @property       #getter using decorator
    def score(self):
        return self._score

    @score.setter   #setter using decorator
    def score(self, score):
        self._score = score

    

    def __str__(self):
        """The __str__ method makes the class instance printable.
        if a Player object is passed in a print statement, it will
        print the string passed in the return statement of the __str__ method"""

        return 'Name: {0.name}, Lives: {0.lives}, Level {0.level}, Score {0._score}'.format(self)