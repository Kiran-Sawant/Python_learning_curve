import subprocess as sub

"""Running the command dir(list all files in directory)
and storing it in p1."""
p1 = sub.run('dir', shell=True, capture_output=True, text=True)

# Printing the results
print(f"stdout: {p1.stdout}")               # returns the output

print(f"stderr: {p1.stderr}")               # returns errors if any

print(f"returncode: {p1.returncode}")       # returns an error code
                                            #0 for no error & 1 for error

# sub.call