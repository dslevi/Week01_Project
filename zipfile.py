#Ex1.py
"""
Unzip files.zip into a directory called 'original_files'

Create 26 directories in current directory
for each letter of the alphabet. (ex. ./a/)

Loop through files in original_files directory and alphabetically organize each into the right sub directory
"""

import os, shutil

current_path = os.getcwd()
unsorted_path = current_path + "/UnsortedFiles"

os.mkdir("./SortedFiles")
sorted_path = current_path + "/SortedFiles"

os.chdir(sorted_path)

#creates a directory in current dir for each letter in alphabet
for x in range(26):
    #creates directory for each letter
    os.mkdir(chr(x + 97))

#sorts through files and places them in appropriate directory

os.chdir(unsorted_path)
unsorted_files = os.listdir(unsorted_path)

for name in unsorted_files:
    first_letter = name[0]
    if os.path.exists(sorted_path + "/" + first_letter):
        shutil.move(unsorted_path + "/" + name, sorted_path + "/" + first_letter)





