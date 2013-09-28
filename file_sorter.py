"""
Before using file_sorter.py,
place files to be sorted into sub-dir titled "UnsortedFiles"

file_sorter.py creates 26 directories, one for each letter of the alphabet,
in a dir called "SortedFiles".

Loops through files in "UnsortedFiles" and places each into the corresponding alphabetic directory
"""

import os, shutil

unsorted_path = os.getcwd() + "/UnsortedFiles"
sorted_path = os.getcwd() + "/SortedFiles"

#removes SortedFiles dir if it already exists (does not work...)
# if os.path.exists(sorted_path):
#   for root, dirs, files in os.walk(sorted_path, topdown=False):
#     for name in files:
#         os.remove(os.path.join(root, name))
#     for name in dirs:
#         os.rmdir(os.path.join(root, name))

#creates SortedFiled dir
os.mkdir(sorted_path)

#Creates a sub-folder for each letter in alphabet in SortedFiles
for x in range(26):
    os.mkdir("SortedFiles/" + chr(x + 97))

#Cycles through list of names of unsorted files and places them alphabetically in appropriate sub-directory
for name in os.listdir(unsorted_path):
    if os.path.exists(sorted_path + "/" + name[0]):
        shutil.move(unsorted_path + "/" + name, sorted_path + "/" + name[0])




