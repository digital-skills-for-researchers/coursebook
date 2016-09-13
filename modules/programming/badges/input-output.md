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

You may use web search to complete this task, but you may not refer to your own previous work. This is to demonstrate that you can solve a task using publicly available resources.

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
Extension: .csv
Location: C:/users/projects/bird-data/data
Size: 30 bytes
Lines: 112
```

**Note:** You may use the web as a reference for this task, including the Python documentation and StackOverflow. You may not refer to your own previous work, even if it is hosted on GitHub.




## Assessor Checklist

- Script runs from shell.
- Prompts the user for a file path.
- Loads a relative file path successfully.
- Loads an absolute file path successfully.
- Produces a summary file with the correct name.
- Summary file contains the correct information.
- Script notifies the user when the summary has been produced.
{:.checklist}

