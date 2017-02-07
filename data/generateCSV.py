"""
Generates csv files out of data files.
Data files must be stored in directories named like DDD-dd (i.e. jan-20)
"""

import os, re, csv, time

dir_pattern = re.compile('\D\D\D-\d\d')  # use only directories like "jan-20"
directories = [x for x in os.walk('.') if dir_pattern.match(os.path.basename(x[0]))]
frequencies = ['100Hz', '500Hz', '900Hz', '1300Hz', '1700Hz', '2100Hz', '2500Hz', '2900Hz', '3300Hz', '3700Hz',
               '4100Hz']

with open('data' + str(int(time.time())) + '.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(('date', 'id') + tuple(frequencies))
    for i in directories:
        path = i[0]
        for file in i[2]:
            lines = [line for line in open(path + os.sep + file, 'r')]
            if len(lines) != 13:
                print("Error in file", file)
            lines = lines[1:12]  # remove first and last line
            lines = [line.rstrip() for line in lines]  # strip newline characters
            print(lines)
            csv_writer.writerow((os.path.basename(path), file) + tuple(lines))
