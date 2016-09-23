#!python3.5
import argparse
import json

from scipy import signal


def convert_files():

    args = parse_command_line_args()
    file_names = get_input_file_names(args)

    process_files(file_names)




def parse_command_line_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", nargs="+", help="Files to be processed", required=True)
    parser.add_argument("-o", help="Output directory", default="jsondata")

    command_line_args = parser.parse_args()

    return command_line_args



def get_input_file_names(command_line_args):

    input_file_names = command_line_args.f
    return input_file_names




def get_output_folder_name(command_line_args):

    output_folder_name = command_line_args.o
    return output_folder_name




def process_files(file_names):

    for file_name in file_names:

        file = open(file_name)
        file_obj = convert_file_to_object(file)
        file.close()

        output_file_name = get_output_file_name(file_name)
        save_object_to_file(file_obj, output_file_name)
    
    display_user_summary(file_names)

    



def convert_file_to_object(file):

    metadata = {}
    readings = []

    for line in file:

        row_data = line.split(',')

        meta_value = get_meta_value(row_data)
        if meta_value : metadata.update(meta_value)
        
        reading = get_reading(row_data)
        if reading : readings.append(reading)
    
    file_object = {
        'metadata': metadata,
        'readings': readings
    }    

    return file_object



def get_meta_value(row_data):

        key = row_data[0]
        value = row_data[1]

        meta_value = None

        if key:
            meta_value = { key: value }

        return meta_value



def get_reading(row_data):

        time = row_data[3]
        voltage = row_data[4]

        reading = None

        if time and voltage:
            reading = {
                'time': time,
                'voltage': voltage
            }

        return reading



def get_output_file_name(file_name):

    output_file_name = file_name + '.out'

    return output_file_name




def save_object_to_file(object, file_name):

    file = open(file_name, 'w')
    json.dump(object, file, indent=4)



def display_user_summary(files):

    file_count = len(files)
    print( file_count, " files reformatted")


convert_files()
