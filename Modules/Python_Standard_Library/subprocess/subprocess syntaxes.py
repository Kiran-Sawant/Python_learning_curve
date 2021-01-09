"""The subprocess module allows you to spawn new processes, connect to
their input/output/error pipes, and obtain their return codes.
    Remember you can grab the outputs on the commandline and not the
outputs of the program itself"""

import subprocess as sub

"""Running the command and storing it in p1."""
path = __file__.replace('subprocess syntaxes.py', 'sys_experiment.py')
script = "python " + path

p1 = sub.run(script, shell=True, stdout=sub.PIPE)

# print(type(p1))

# Printing the output on commandline.
print(f"stdout: {p1.stdout}")

print(f"stderr: {p1.stderr}")               # returns error code

print(f"returncode: {p1.returncode}")       # returns an error code
                                            # 0 for no error & 1 for error

k = eval(p1.stdout)
print((type(k)))