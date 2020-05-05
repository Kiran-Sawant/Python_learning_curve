def line():
    print("this sentence is from {} module".format(__name__))


def line_2(name):
    '''Takes the current module name as an argument in a string format'''
    print('\nthis line is called from {} module'.format(name))

if __name__ == '__main__':
    line()
    line_2('module_1')
