"""shutils supports zip, tar, gztar, bztar, xztar compression formats."""

import shutil

# Creating an archive
shutil.make_archive('another_file', 'zip', 'my_zip')      # pass archive name, format & file name

# Extracting an archive
shutil.unpack_archive('another_file.zip', 'another')      # pass archive name & folder name