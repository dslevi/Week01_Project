"""
Before using file_sorter.py,
place files to be sorted into a sub-dir titled "UnsortedFiles"

file_sorter.py creates 26 directories, one for each letter of the alphabet,
in a dir called "SortedFiles".

Loops through files in "UnsortedFiles" and places each into the corresponding alphabetic directory
"""

import os, shutil

current_path = os.getcwd()
unsorted_path = current_path + "/UnsortedFiles"
sorted_path = current_path + "/SortedFiles"

#removes SortedFiles dir if it already exists (does not work if full...)
#if os.path.exists(sorted_path):
#   os.removedirs(sorted_path)

#creates SortedFiled dir and cds into it
os.mkdir("./SortedFiles")
os.chdir(sorted_path)

#Creates a sub-folder for each letter in alphabet in SortedFiles
for x in range(26):
    os.mkdir(chr(x + 97))

#Cycles through list of names of unsorted files and places them alphabetically in appropriate sub-directory
unsorted_files = os.listdir(unsorted_path)

for name in unsorted_files:
    first_letter = name[0]
    if os.path.exists(sorted_path + "/" + first_letter):
        shutil.move(unsorted_path + "/" + name, sorted_path + "/" + first_letter)





