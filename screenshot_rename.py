import numpy as np
import os

"""
    This code renames every screenshot in the current directory to
    Figure_X.png in the correct order, i.e., the number X increases
    when the screenshots are done later in time.

    In this version, the code works on multiple screenshots performed
    on the same day and uses the time of the screenshot to sort and rename.

    - Step 1: Read the files on the directory using the os library and save
              them into a string list str_list.
    - Step 2: Remove files that are not wished to rename.
    - Step 3: Clone the list of strings.
    - Step 4: Read the times of the screenshots and create an array of
              string to int.
    - Step 5: Use the argsort function to obtain an array of sorted elements.
    - Step 6: Rename every element to "Figure" + index + ".png" according to
              the sorted elements using os.rename

"""

# Read files on directory and save them to str_list
str_list = os.listdir()

# Remove undesired files
str_list.remove('.DS_Store')
str_list.remove('screenshot_rename.py')

# Clone list for later use, keeps names of files
str_list_0 = str_list[:]

# Loop to read all the times of the screenshots
for i in range(len(str_list_0)):
    a = str_list_0[i][-12:-4]       # Take the time strings before .png
    b = a.replace(".","")           # Remove dots to have only numbers
    str_list[i] = int(b)            # Convert numbers into ints

# Create a list of sorting indices
sortlist = np.argsort(str_list)

# Create the initial and final strings to rename files
output = ['Figure_','.png']

# Loop to rename every file according to the indices
for i in range(len(str_list)):
    s = str(i + 1)                              # Create index string
    string = s.join(output)                     # Join it to the output terms
    os.rename(str_list_0[sortlist[i]], string)  # Rename every element
