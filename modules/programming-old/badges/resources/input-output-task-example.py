#!python3.5

from pathlib import Path

# CONSTANTS #######################

FILE_PATH_PROMPT = "Please enter the path of a file to summarise: "
FILE_PATH_INVALID = "Sorry, that's not a valid file path."

# VARIABLES ##################

file_path = None



# FUNCTIONS ##################

'''
Prompts the user for a file path.

If the path exists and is a file,
return a Path object.

If the path is not a file, inform the user
and prompt them again for a file path.
'''
def get_file_path():
    
    user_input = input(FILE_PATH_PROMPT)
    path = Path(user_input)
    is_file = path.is_file()
    
    if not is_file:
        print()
        path = None
    
    return path


def get_summary(file_path):
    
    # find the file name without the extension
    file_name = file_path.stem
    
    # find the file extension
    file_extension = file_path.suffix

    # find the absolute path to the parent folder
    parent_folder = file_path.parent
    
    # find the file size in bytes
    file_size = file_path.stat().st_size
    
    # find the number of lines
    line_count = get_line_count(file_path)
    
    summary_template = (
        "file name: {0} \n"
        "extension: {1} \n"
        "location: {2} \n"
        "size: {3} bytes\n"
        "lines: {4}"
    )
    
    summary = summary_template.format(
        file_name,
        file_extension,
        parent_folder,
        file_size,
        line_count
    )
    
    return summary
    

def get_line_count(file_path):
    
    # open the file
    file = file_path.open()

    # count the lines
    line_count = 0
    for line in file:
        line_count += 1
    
    # close the file
    file.close()
    
    return line_count
    
    
def get_summary_file_path(file_path):
    
    file_name = file_path.stem + '.summary' + file_path.suffix
    file_path = file_path.parent.joinpath('/' + file_name)
    return file_path
    
    
def save_to_file(content, file_path):
    
    print(content)

    file = Path(file_path)
    file.touch()
    file.write_text(content)
    
    

# WORKFLOW ###################



# get the file path from the user
while file_path == None:
    file_path = get_file_path()

# get the summary
summary = get_summary(file_path)

# get the file name to save to
summary_file_name = get_summary_file_path(file_path)

# save to file
save_to_file(summary, summary_file_name)
    





    



# generate the summary

# save the summary







# FUNCTIONS ####################

def get_number_of_lines_in_file(file_name):
    with open(file_name) as file:
        for line_number, line_content in enumerate(file):
            pass
    return line_number + 1