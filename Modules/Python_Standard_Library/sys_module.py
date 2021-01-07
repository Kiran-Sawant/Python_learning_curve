"""The sys module can be used to access this script externally through the shell.
both sys & subprocess modules can be used to communicate between two different
languages through the shell.
    sys is used to make a script that will recieve commands from the shell.
    subprocess is used to make a script that will send commands to the shell."""

import sys

sys.stderr.write("This is how stderr text looks\n")
sys.stderr.flush()
sys.stdout.write("This is how stdout text looks\n")

#________________sys.argv attribute__________________#
""" .argv is a list of all arguments passed from the shell.
To execute the current script from shell use the following command:
python sys_module.py "Hello", "Its me"
here, sys_module.py, "Hello" & "Its me" are arguments."""

# print(f"The first argument is: {sys.argv[0]}")
for i in sys.argv:
    print(i)