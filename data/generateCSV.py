"""
Generates csv files out of data files.
Data files must be stored in directories named like DDD-dd (i.e. jan-20)
"""

import os, re, csv, time, string

def getAsciiIdString(n):
    first =  string.ascii_lowercase[int(n / 26)]
    second = string.ascii_lowercase[n % 26]
    return first+second

# __time_str = str(int(time.time()))
# data_filename = 'data' + __time_str + '.csv'
# data_plot_filename = 'data_plot' + __time_str + '.csv'
data_filename = 'data.csv'
data_plot_filename = 'data_plot.csv'

dir_pattern = re.compile('\D\D\D-\d\d')  # use only directories like "jan-20"
directories = [x for x in os.walk('.') if dir_pattern.match(os.path.basename(x[0]))]
frequencies = [100, 500, 900, 1300, 1700, 2100, 2500, 2900, 3300, 3700, 4100]

# initialise empty data store
data = {}
for f in frequencies:
    data[f] = []

with open(data_filename, 'w') as data_file:
    data_writer = csv.writer(data_file)
    data_writer.writerow(('date', 'id') + tuple(frequencies))
    for i in directories:
        path = i[0]
        for file in i[2]:
            lines = [line for line in open(path + os.sep + file, 'r')]
            if len(lines) != 13:
                print("Error in file", file)
            lines = lines[1:12]  # remove first and last line
            lines = [line.rstrip() for line in lines]  # strip newline characters
            data_writer.writerow((os.path.basename(path), file) + tuple(lines))
            for i, datapoint in enumerate(lines):
                data[frequencies[i]].append(datapoint)


with open(data_plot_filename, 'w') as data_plot_file:
    data_plot_writer = csv.writer(data_plot_file)
    id_characters = []
    for i in range(0, len(data[100])):
        print(i, getAsciiIdString(i))
        id_characters.append(getAsciiIdString(i))

    # id_characters = getAsciiIdString()list(string.ascii_lowercase[0:len(data[100])])  # get id characters
    data_plot_writer.writerow(('frequenz',) + tuple(id_characters))
    for f in frequencies:
        data_plot_writer.writerow((f,) + tuple(data[f]))
        print(f, data[f])

