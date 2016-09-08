---
layout: badge
title: Input and Output
---

# Input and Output
_Working with prompts and files in Python_

## Description

Using Python, write a script to ask the user for a file to process, then save the program's output to another file.



## Student Task

This task is designed to assess whether you understand how to write Python code for input and output via the shell, and how to read and write plain text files.

You may seek help with parts of the code not related to shell input/output or file input/output if needed.

You may assume that the source file will always be a text file.


<br>


1. Create a new script called `input-output.py`.

2. Prompt the user for the path to a file to process.

4. Create a summary of the file in the same directory. The summary file should have the same name as the source file, with the additional extension `.summary`. eg. a summary of `bird-data.csv` would be called `bird-data.csv.summary`

5. The format for the summary file is included below.
  
6. Notify the user when the summary has been created.

<br>

**Note:** The summary file should be formatted as follows:

```text
Filename: bird-data
Extension: csv
Size: 30kb
Lines: 112
```

**Note:** You may use the following function to count the number of lines in a text file:

```python
def get_number_of_lines_in_file(file_name):
    with open(file_name) as file:
        for line_number, line_content in enumerate(file):
            pass
    return line_number + 1
```




## Assessor Checklist

- Script runs from shell.
- Prompts the user for a file path.
- Loads a relative file path successfully.
- Loads an absolute file path successfully.
- Produces a summary file with the correct name.
- Summary file contains the correct information.
- Script notifies the user when the summary has been produced.
{:.checklist}

<br>

**Note:** The student may ask for help coding and executing the parts of the Python file unrelated to shell input/output or file input/output.

They will need to independently find the file, open it, separate the file name from the extension, find the file size, create the output, and save the output file.

The line count function is provided. They may ask for help calling the function but should not need to.

