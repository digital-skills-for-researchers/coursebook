---
layout: page
title: Input and Output
---

Using Python, write a script to ask the user for a file to process, then save the program's output to another file.




## Project-Based Assessment

For this assessment, you can use file read/write functionality in your existing project code as evidence of understanding.

You will need to show the code to your mentor and then answer the questions described under "Assessment Questions" below.





## Task-Based Assessment

This task is designed to assess whether you understand how to write Python code for input and output via the shell, and how to read and write plain text files.

You may use web search to complete this task, including the Python documentation and StackOverflow. All research and compilation of the code must be your own work.

You may assume that the source file will always be a text file.




1. Right-click and save the sample data file `TEK000.CSV` from [here](resources/TEK000.CSV).

1. Create a new script called `input-output-task.py`.

2. Prompt the user for the path to a file to process.

4. Create a summary of the file in the same directory. The summary file should have the same name as the source file, with the additional extension `.summary`. eg. a summary of `bird-data.csv` would be called `bird-data.csv.summary`

5. The format for the summary file is included below.
  
6. Notify the user when the summary has been created.


**Note:** The summary file should be formatted as follows:

```text
Filename: bird-data
Extension: .csv
Location: C:/users/projects/bird-data/data
Size: 30 bytes
Lines: 112
```

[View Assessor Guide](input-output-guide.html)


## Assessor Checklist

1. Script runs from shell.
2. Prompts the user for a file path.
3. Loads a relative file path successfully.
4. Produces a summary file with the correct name.
5. Summary file contains the correct information.
6. Script notifies the user when the summary has been produced.

