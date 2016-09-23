#!python3.5
import argparse
import json

class NLDLParser():

    input_files = None
    output_directory = None

    data = None




    def __init__(self):

        self.parse_command_line_args()

        if self.input_files:
            print("there are files yay", self.input_files)
            #self.parse_files(self.input_files)





    # PUBLIC #####################################

    # parse a single file
    def parse_file(self, file_path):

        print("parse_file", file_path)

        self.process_files([file_path])
        return self.data[0]


    # parse multiple files
    def parse_files(self, file_paths):

        self.process_files(file_paths)
        return self.data


    

    # PRIVATE #####################################


    def parse_command_line_args(self):

        parser = argparse.ArgumentParser()

        parser.add_argument("--files", nargs="+", help="Files to be processed")
        parser.add_argument("--outdir", help="Output directory", default="jsondata")

        command_line_args, unknown_args = parser.parse_known_args()

        self.input_files = command_line_args.files
        self.output_directory = command_line_args.outdir




    def process_files(self, file_names):

        self.data = []

        for file_name in file_names:

            file = open(file_name)

            file_obj = self.convert_file_to_object(file)
            self.data.append(file_obj)

            file.close()

            output_file_name = self.get_output_file_name(file_name)
            self.save_object_to_file(file_obj, output_file_name)
        
        self.display_user_summary(file_names)

        



    def convert_file_to_object(self, file):

        metadata = {}
        readings = []

        for line in file:

            row_data = line.split(',')

            meta_value = self.get_meta_value(row_data)
            if meta_value : metadata.update(meta_value)
            
            reading = self.get_reading(row_data)
            if reading : readings.append(reading)
        
        file_object = {
            'metadata': metadata,
            'readings': readings
        }    

        return file_object



    def get_meta_value(self, row_data):

            key = row_data[0]
            value = row_data[1]

            meta_value = None

            if key:
                meta_value = { key: value }

            return meta_value



    def get_reading(self, row_data):

            time = row_data[3]
            voltage = row_data[4]

            reading = None

            if time and voltage:
                reading = {
                    'time': time,
                    'voltage': voltage
                }

            return reading



    def get_output_file_name(self, file_name):

        output_file_name = file_name + '.out'

        return output_file_name




    def save_object_to_file(self, object, file_name):

        file = open(file_name, 'w')
        json.dump(object, file, indent=4)



    def display_user_summary(self, files):

        file_count = len(files)
        print( file_count, " files reformatted")

