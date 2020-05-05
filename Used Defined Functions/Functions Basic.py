def python_food():          #Initiating a function by the name python_food()
    print('spam and eggs')

#calling a function
python_food()

def centre_text(*args):      #giving the parameter for the function in parenthesis,
                             #* means there can be multiple argument passed in one call
    text = ''
    for arg in args:
        text += str(arg) + ' '
    leftMargin = (80 - len(text)) // 2
    print(' ' * leftMargin, text)

centre_text('spam and eggs')           #the arguments are assigned to the parameter of the function
                                       #then the defined operation is carried out on the argument and an output is passed
centre_text('call', 'me', 'maybe?')    #passing multiple arguments to a single parameter
centre_text(6996)