
"""
Programe name: add_quation_marks_extensions_list.py
Author: Hao Wang
Version: 1.0
Date: 2024-10-14
Purpose: This script reads the file called 'extensions.list', adds quotation marks around each line,
         and writes the modified content back to the file.
         The file "extensions.list has all the VS Code extensions installed on my local. I use the command:

         code --list-extensions > extensions.list

         in VS Code PowerShell/CMD terminal to create. 
"""

# Open the file in read mode
with open('extensions.list', 'r') as file:
    # Read all lines from the file
    extensions = file.readlines()

# Print each extension
for extension in extensions:
    print(extension.strip())

# Open the file in write mode to save the modified content
with open('extensions.list', 'w') as file:
    # Iterate over each extension and add quotation marks
    for extension in extensions:
        # Strip any leading/trailing whitespace and add quotation marks
        modified_extension = f'"{extension.strip()}"'
        # Write the modified extension back to the file
        file.write(modified_extension + '\n')

print("Quotation marks have been added to each line in the extensions.list file.")