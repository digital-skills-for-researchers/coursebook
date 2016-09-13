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

# loop over all readings in the list
for reading in readings:

    # get the temp as a number
    temp = float(reading['temp'])

    # on first time around, initialise each
    # of the max and min values to the values
    # from the current reading as a start point
    if min_temp == None:
        min_temp = temp
        max_temp = temp

    # compare to min temp
    if temp < min_temp:
        min_temp = temp

    # compare to max temp
    if temp > max_temp:
        max_temp = temp

    all_temperatures.append(temp)

# end for reading in readings





# Calculate the total -----------

# count the number of readings in the list
reading_count = len(readings)




# Calculate the median -----------

# order the readings based on temp
all_temperatures.sort()

# decide if the number of elements is odd
odd_reading_count = (reading_count % 2 == 1)

# find the median of the list
median_time_between_readings = None
median_index = floor(reading_count / 2)

# for an odd count, use the middle item
if odd_reading_count == True:
    median_temp = all_temperatures[median_index]

# for an even count, use the average
# of the two middle items
else:
    temp_1 = all_temperatures[median_index]
    temp_2 = all_temperatures[median_index + 1]
    median_temp = (temp_1 + temp_2) / 2




# Calculate the range -----------

# calculate temperature range
temp_range = max_temp - min_temp





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