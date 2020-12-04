"""Here, html_tag is a first-class function that can be assigned to a variable(line 12),
   passed as an argument(line 12, 14, 16), return these functions from other functions
   remember!, First-class function must return the enclosing function & mustn't execute it."""

def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
        
    return wrap_text            #don't use parenthesis after function name

print_h1 = html_tag('h1')       #assigning a variable to a firstclass function

'''The parameter passed to the variable is then passed to the enclosed function of the
   firstclass function. Hence, the variable acts as the enclosed function'''

print_msg1 = print_h1('Hello')  #using a Closure function
print_msg2 = print_h1('My name is Kiran')
print_msg3 = print_h1("I am learning Python")