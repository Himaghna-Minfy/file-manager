# file-manager

🗂️ Python File Manager
A simple file manager built using Python’s os module, allowing you to manage files and directories through custom shell-like commands.

📦 Features
This file manager supports basic filesystem operations:

Command	Description
cwd	Displays the current working directory
ls	Lists files and folders in the current directory
cd <path>	Changes the working directory to <path>
mkdir <folder>	Creates a new folder with the specified name
touch "<file>" "<content>"	Creates a file with optional content (quotes required)
rm <file>	Deletes the specified file
exit	Exits the file manager

🚀 Getting Started
1. Requirements
Python 3.x

2. Run the File Manager
bash
Copy
Edit
python file_manager.py
🧪 Usage Examples
text
Copy
Edit
>>> cwd
/home/user/projects

>>> ls
file1.txt
my_folder

>>> mkdir "new_folder"

>>> cd new_folder

>>> touch "notes.txt" "Hello, this is a file."

>>> ls
notes.txt

>>> rm notes.txt

>>> exit
📝 Note: For the touch command, both the filename and content must be enclosed in double quotes if the content is included.

📁 File Structure
bash
Copy
Edit
file_manager.py   # Main file manager script
README.md         # Project documentation
✅ Input Parsing
The program uses basic string parsing to split commands.

For touch, double quotes are required around the filename and content.

Handles missing arguments silently (basic validation included).
