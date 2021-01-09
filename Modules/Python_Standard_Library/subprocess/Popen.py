"""The underlying process creation and management in this module is handled
by the Popen class. It offers a lot of flexibility so that developers are
able to handle the less common cases not covered by the convenience functions.

    In this script we run a command suing Popen set the standard output to
PIPE which returns the output as a bytestream."""

import subprocess as sub

path = __file__.replace('Popen.py', 'sys_experiment.py')
script = "python " + path

"""Running the command and storing it in p1."""
p1 = sub.Popen(script, stdout=sub.PIPE)

# Interact with the process
output, error = p1.communicate()

# Check if child process is terminated.
p1.poll()

# wait for the child process to terminate.
p1.wait(timeout=120)

# Kills the child process.
p1.terminate()
p1.kill()

# Arguments passed to Popen.
p1.args

# childs process ID.
p1.pid

# childs return code.
p1.returncode