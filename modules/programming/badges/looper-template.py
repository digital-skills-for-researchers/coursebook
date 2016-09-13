#!python3.5
from math import floor

readings = [
    {'time': '2016-03-11 13:02:53', 'temp': '12.3'},
    {'time': '2016-03-11 13:03:55', 'temp': '12.5'},
    {'time': '2016-03-11 13:05:33', 'temp': '12.7'},
    {'time': '2016-03-11 13:08:20', 'temp': '12.9'},
    {'time': '2016-03-11 13:09:11', 'temp': '13.3'},
    {'time': '2016-03-11 13:11:01', 'temp': '14.0'},
    {'time': '2016-03-11 13:13:34', 'temp': '13.8'},
    {'time': '2016-03-11 13:12:26', 'temp': '13.7'},
    {'time': '2016-03-11 13:17:53', 'temp': '13.8'},
    {'time': '2016-03-11 13:18:24', 'temp': '14.1'},
    {'time': '2016-03-11 13:20:44', 'temp': '13.5'},
    {'time': '2016-03-11 13:21:22', 'temp': '13.6'},
    {'time': '2016-03-11 13:23:56', 'temp': '13.1'},
    {'time': '2016-03-11 13:25:00', 'temp': '12.8'},
    {'time': '2016-03-11 13:26:15', 'temp': '12.5'}
]


# VARIABLES #########################

reading_count = None
max_temp = None
min_temp = None
median_temp = None

all_temperatures = []




# CALCULATIONS #######################


# Calculate the max and min -----------

min_temp = 0
max_temp = 0





# Calculate the total -----------

reading_count = 0




# Calculate the median -----------

median_temp = 0




# Calculate the range -----------

temp_range = 0





# OUTPUT ############################

# output results
results_template = (
    "Total Readings: {0}\n"
    "Max Temp: {1} C\n"
    "Min Temp: {2} C\n"
    "Median temp: {3} C\n"
    "Temp Range: {4} C"
)

# format the results
results = results_template.format(
    reading_count,
    max_temp,
    min_temp,
    median_temp,
    temp_range
)

# print the results
print(results)

