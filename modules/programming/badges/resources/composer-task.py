#!python3.5
import argparse
import json



# Support command line arguments --------
parser = argparse.ArgumentParser()

parser.add_argument("-f", nargs="+", help="Files to be processed", required=True)
parser.add_argument("-o", help="Output directory", default="jsondata")

command_line_args = parser.parse_args()


# Extract the input file names ----------
input_file_names = command_line_args.f


# Extract the output folder name --------
output_folder_name = command_line_args.o


# Process each file ----------
for file_name in input_file_names:
    
    # Open file --------------------
    file = open(file_name)

    # Extract Values from Lines ----------
    header_info = {}
    readings = []

    for line in file:

        # Convert text line to column list
        columns = line.split(',')

        # extract header info
        key = columns[0]
        value = columns[1]

        if key:
            header_info[key] = value
        
        # extract reading data
        time = columns[3]
        voltage = columns[4]

        if value_1 and value_2:
            reading = {
                'time': value_1,
                'voltage': value_2
            }
            
            readings.append(reading)


    # Close the input file
    file.close()


    # Create New File Name ---------
    output_file_name = file_name + '.out'


    # Build Data object
    output_data = {
        "header": header_info,
        "data": readings
    }

    # Export Data To File ----------
    output_file = open(output_file_name, 'w')
    json.dump(output_data, output_file, indent=4)



# Summary for user ----------
file_count = len(input_file_names)
print( file_count, " files reformatted")
