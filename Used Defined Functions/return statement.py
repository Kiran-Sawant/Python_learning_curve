'''return statement, states the output of the function
which is then returned to wherever it was called from
in return statement use '+' insted of a ',' to add multiple values'''
#______________defining the function__________#
def centre_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep
    leftMargin = (80 - len(text)) // 2
    return ' ' * leftMargin + text

#_______________Writing to file________________#
with open('centre.txt', mode='w') as myFile:
    print(centre_text('call me maybe?'), file=myFile) #printing the output of centre_text() for given arg in a file
    s = centre_text('Carnival of Rust')               #storing the output of centre_text() in a variable
    print(s, file=myFile)
