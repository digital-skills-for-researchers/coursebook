# Python 3

# CONSTANTS #######################

FILE_PATH_PROMPT = 'Please enter the path of a file to summarise: '



# WORKFLOW ###################

# prompt the user for a filepath
file_path = input(FILE_PATH_PROMPT)

print("file path", file_path)


# open the file
file = open(file_path)

# find the absolute path to the parent folder


# find the file name without the extension

# find the file extension

# count the lines
line_count = 0
for line in file:
    line_count += 1

print("line count: ", line_count)

# close the file
file.close()


# generate the summary

# save the summary







# FUNCTIONS ####################

def get_number_of_lines_in_file(file_name):
    with open(file_name) as file:
        for line_number, line_content in enumerate(file):
            pass
    return line_number + 1