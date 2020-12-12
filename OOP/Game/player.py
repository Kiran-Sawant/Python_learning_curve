"""     Learning getters, setters and property.
Sometimes there are attributes in a class that are not meant to be shown directly or
not allowed to be modified directly or maybe both called hidden variable (a.k.a private variable).
A getter method returns the value of a hidden variable.
A setter method sets the value of a variable to the passed argument.
One can pass conditional statements in the getters and setters as well.
If a variable is not meant to be changed, don't make a setter method for it.
If a variable is not meant to be displayed, don't make a getter method for it.

The inbuilt property() method returns a property objects that can be assigned to
variables. Property can takes 4 arguments, getter method, a setter method, delete
method and a doc string. Only the properties passed in the property method are 
available to that variable."""

class Player(object):
    """creates a player object.
    
    Attributes:
        name (str): Name of the player.
        _lives (int): Number of attempts till game over.
        _level (int): stage @ which player is playing.
        _score (int)"""

    def __init__(self, name: str):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    #_____getters & setters for lives_____#
    def _get_lives(self):           #Getter for _lives
        return self._lives

    def _set_lives(self, lives: int):    #Setter for _lives
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

    """With these properties one can do player_object.lives=n to set lives
    or player_object.lives to retrive lives."""
    lives = property(fget=_get_lives, fset=_set_lives) # If only a getter is mentioned the attribute becomes read only.
    level = property(fget=_get_level, fset=_set_level) # If only a setter is mentioned the attribute becomes write only.
                                                       # If a delete method is not passed one cannot delete the attribute.
    
    #_____getters & setters using decorators______#
    @property       #getter using decorator
    def score(self):
        return self._score

    @score.setter   #setter using decorator
    def score(self, score):
        self._score = score

    

    def __str__(self):
        """The __str__ dunder/magic method makes the class instance printable.
        if a Player object is passed in a print statement, it will
        print the string passed in the return statement of the __str__ method"""

        return 'Name: {0.name}, Lives: {0.lives}, Level {0.level}, Score {0._score}'.format(self)