---
layout: default
title: Born to Shell | Shell Scripting
subtitle: 

introduction: |

  Create a shell script that generates a new Python project based on a provided project name.

  To claim this badge, you must demonstrate your knowledge by writing the script and having it reviewed by a mentor.

---


## Student Task

Create a new shell script called `create-python-project.sh`. The script should take a project name from the user and use that project name to generate the project starter files.


<br>


1. Create a shell script called `create-python-project.sh`.

2. The script should expect a project name from the user. 

3. The project name can be taken as a parameter OR the script can prompt the user for the project name (your choice).

4. The project name eg. "My Cool Project" must be converted to kebab case eg. "my-cool-project" for use in file names and folder names.

5. The script should generate a project folder with the name provided.

6. The project folder should contain a file `README.md` which contains the [Project Name] as a heading, and a paragraph saying "Project description goes here."

7. The project folder should contain a file `[project-name].py` which prints "Hello from [Project Name]" when executed.

8. The project folder should contain a subfolder called `data` which contains a blank file named `.gitkeep`.

9. The project folder should be managed with Git.

10. The script should give the user feedback as each step is completed.

11. The script should give the user feedback when the script's tasks are all complete.


<br>


**Note:** This script only needs to be compatible with either Windows or Ubuntu/OSX. It does not need to support both systems.


## Assessor Checklist

1. Script executes without error.
2. Correct directory and file structure is generated.
3. Readme file is Markdown-formatted and has correct content.
4. Data folder contains a hidden `.gitkeep` file.
5. Python file executes successfully.
6. Script converts supplied project name to lowercase with hyphens in place of spaces.
7. Project folder is an initialised Git repository.
8. Script is well-commented.
9. Script uses whitespace (new lines) to visually group tasks.