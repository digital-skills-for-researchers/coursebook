#!python3.5
from math import floor
from datetime import datetime

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

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

reading_count = 0
earliest_time = None
latest_time = None
time_range = None
max_temp = None
min_temp = None

seconds_between_readings = []
previous_reading_time = None

for reading in readings:

    # count the reading
    reading_count += 1

    # get the time as a datetime
    time = datetime.strptime(reading['time'], TIME_FORMAT)

    # get the temp as a number
    temp = float(reading['temp'])

    # on first time around, initialise each
    # of the max and min values to the values
    # from the current reading as a start point
    if reading_count == 1:
        earliest_time = time
        latest_time = time
        min_temp = temp
        max_temp = temp

    # seconds since last reading
    if previous_reading_time:
        seconds_since_last_reading = time - previous_reading_time
        seconds_between_readings.append(seconds_since_last_reading)

    previous_reading_time = time
    
    # compare to earliest time
    if time < earliest_time:
        earliest_time = time

    # compare to latest time
    if time > latest_time:
        latest_time = time

    # compare to min temp
    if temp < min_temp:
        min_temp = temp

    # compare to max temp
    if temp > max_temp:
        max_temp = temp

    
# order the times between readings
seconds_between_readings.sort()

# decide if the number of elements is odd
odd_number_of_readings = (reading_count % 2 == 1)

# find the median of the list
median_time_between_readings = None
median_index = floor(reading_count / 2)

if odd_number_of_readings == True:
    median_time_between_readings = seconds_between_readings[median_index]
else:
    median_time_between_readings = seconds_between_readings[median_index] + seconds_between_readings[median_index+1]


# calculate temperature range
temp_range = max_temp - min_temp


# output results
results_template = (
    "Total Readings: {0}\n"
    "Time Range: {1} to {2}\n"
    "Median time between readings: {3} seconds\n"
    "Max Temp: {4} C\n"
    "Min Temp: {5} C\n"
    "Temp Range: {6} C"
)

results = results_template.format(
    reading_count,
    earliest_time,
    latest_time,
    median_time_between_readings,
    max_temp,
    min_temp,
    temp_range
)

print(results)

