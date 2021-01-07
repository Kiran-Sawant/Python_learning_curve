import zipfile as zip_

# Creating a zip file
my_zip = zip_.ZipFile("files.zip", mode='w', compression=zip_.ZIP_DEFLATED)

my_zip.write('The Idiot.epub')
my_zip.write('Notes from the underground.pdf')

print(my_zip.getinfo('The Idiot.epub'))

my_zip.close()

# Reading a zip file
with zip_.ZipFile("files.zip", mode='r') as file:
    print(file.namelist())                        # Gives a list of all files in the archive
    file.extractall('my_zip')                     # Extracting all files in the passed folder
    file.extract('The Idiot.epub')                # Extracting a specific file

print(zip_.is_zipfile('files.zip'))
