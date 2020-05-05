'''args stands for arguments, ie. the values around which the function is going to perform its operation.
kwargs stand for keyword arguments, these parameters have a keyword assigned to it while initializing the function,
and while calling the funtion these keys are needed to me mentioned for passing values to kwargs. usually args are
the core data while kwargs are used for moderation. one can pass multiple args to a single parameter but only a single
values to a single kwarg. kwargs have a default value if a kwarg is not mentioned while calling the function'''

def centre_text(*args, sep=' ', end='\n', file=None, flush=False):      #accepting multiple arguments for a single parameter args
                                                                        #sep, end, file, flush are keyword arguments with their default values
    text = ''
    for arg in args:
        text += str(arg) + sep
    leftMargin = (80 - len(text)) // 2
    print(' ' * leftMargin, text, end=end, file=file, flush=flush)

centre_text('call', 'me', 'maybe?', sep='.')                            #calling function by passing multiple args and kwargs using key

'''while passing kwargs the value must be of same datatype as defined in the function
   if kwargs are not passed the default values are assigned in the function'''