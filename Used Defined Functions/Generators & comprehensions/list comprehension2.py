def centre_text(*args):

    # text = ""  
    # for arg in args:
    #     text += str(arg)
    text = "-".join([str(arg) for arg in args])     # Using list comprihension
    leftMargin = (80 - len(text)) // 2
    print(' ' * leftMargin, text)

centre_text('spam and eggs')

centre_text('call', 'me', 'maybe?')
centre_text(6996)