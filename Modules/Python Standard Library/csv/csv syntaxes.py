import csv

#____________Using CSV reader & writer methods______________#
with open('names.csv', mode='r') as csv_file:
    read = csv.reader(csv_file)                             # Creating a CSV reader object

    with open('new_file.csv', mode='w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')   # Creating a CSV writer object

        for line in read:
            csv_writer.writerow(line)                       # Writing to an external file

#____________Using DictReader_________________#
"""DictReader returns an ordered dictionary where
    the CSV headers are used as keys"""

with open('names.csv', mode='r') as csv_file:
    read = csv.DictReader(csv_file)

    # converting a csv_reader object to a CSV file.
    with open('new_file2.csv', mode='w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()      # command to write header info the CSV file

        for line in read:
            csv_writer.writerow(line)