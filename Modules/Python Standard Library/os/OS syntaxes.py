import os

# Getting current working directory
curr_dir = os.getcwd()
print(curr_dir)

# Changing current working directory
os.chdir("C:\\Users\\Tony_Stark\\Desktop\\")

print(os.getcwd())      # print current working directory

# Creating directories
os.mkdir("New_folder")                  # for single folder
os.makedirs("New\\old")                 # for nested folders use \\ in windows

# listing all files and folders
print(os.listdir())

# Deleting Directories
os.rmdir("New_folder")
os.removedirs("New\\old")

# Renaming Files
os.rename('My Work.txt', 'Work.txt')

# getting Info of files as named tuple
file_info = os.stat('Work.txt')
print(file_info)

# Traversing current file
walk = os.walk(os.getcwd())         # os.walk() is a generator

for dirpath, dirnames, filenames in walk:
    print("Curent Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()

# Accessing Environment Variables
"""os.environ returns a dictionary of all environment variables"""

k = os.environ['HOME']

# Creating a valid file path
"""path module in os has several methods to work with directory paths"""

file_path = os.path.join(k, 'test.txt')
print(file_path)

os.path.exists(os.getcwd())        # Checks if the path exists
os.path.isfile(os.getcwd())        # Checks if the passed path leads to a file
os.path.isdir(os.getcwd())         # Checks if the passed path leads to a folder
os.path.splitext("C:\\Users\\Tony_Stark\\Desktop\\Work.txt")      # splits the extension and rest of the path
