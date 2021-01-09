"""subprocess module can be used to invoke external programs(subprocesses) through OS shell.
This script invokes another python script through shell, using the .run() method.
One can invoke scripts written in other languages as well in the same way."""

import subprocess as sub

# setting the path of target script.
path = __file__.replace('subprocess example.py', 'sys_expriment.py')
# setting the script to run.
script = "python " + path

# print(path)
# print(script)

# running the script in OS default shell.
sub.run(script, shell=True)
