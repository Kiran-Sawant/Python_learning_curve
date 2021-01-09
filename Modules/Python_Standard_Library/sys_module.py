""" The module provides access to some variables used by the interpreter to
function and interact with the interpreter.
    The sys module can be used to access this script externally through the shell.
both sys & subprocess modules can be used to communicate between two different
languages through the shell.
    sys is used to make a script that will recieve commands from the shell.
    subprocess is used to make a script that will send commands to the shell.
    This script shows some useful variables.
PyDoc: https://docs.python.org/3.7/library/sys.html"""

import sys
import pprint

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

#____names of all modules compiled in python interpreter_____#
print(sys.builtin_module_names)

#____Gives the absolute path of python interpreter______#
print(sys.executable)

#____size of the object in bytes______#
print(sys.getsizeof("Get_off_my_lawn"))

#___names of all the loaded modules___#
pprint.pprint(sys.modules)

#__list of paths where interpreter searches for modules__#
print(sys.path)

#____string containing info of platform (OS)______#
print(sys.platform)
# check if the OS is windows
print(sys.platform.startswith('win32'))
# check if the OS is linux
print(sys.platform.startswith('linux'))

#___returns python interpreter version_____#
print(sys.version)

#____returns C API version_____#
print(sys.api_version)

#_____shutsdown the interpreter____#
sys.exit()
