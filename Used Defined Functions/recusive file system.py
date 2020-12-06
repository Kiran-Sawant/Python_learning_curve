import os

#_____Recursive methods in file Systems______#
def list_directories(s):

    def dir_list(d):                                        # A method inside of a method
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):                  # If it encounters a directory inside a directory.
                print('\t' * tab_stop + 'directory: ' + f)
                tab_stop += 1
                dir_list(current_dir)                       # Calling the same method recursively.
                tab_stop -= 1
            else:                                           # If there are no directories in a directory.
                print('\t' * tab_stop + 'file: ' + f)
    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of "+ s)
        dir_list(s)
    else:
        print(s +" Does not exist!")

list_directories(r'H:\Songs\Trance')