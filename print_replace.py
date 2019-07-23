"""

    This file contains some utilities regarding printing.
    They are useful to manipulate prints and, in the ML context,
    to define interesting callbacks.

    The code will print "Loading" and introducing dots every second.
    Right after all the desired prints are in the output, the print shall
    erased. This procedure is performed twice.

"""

# Import time and sys libraries
import time
import sys

# Define the commands to control terminal outputs.
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
sys.stdout.write(CURSOR_UP_ONE)
sys.stdout.write(ERASE_LINE)

# Define function that deletes the last lines (n)
def delete_last_lines(n = 1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


# Initialise iteration loop (2 iterations)
for i in range(0,2):
    # Initialise printing loop
    for x in range (0,5):             # Maximum of 5 dots in the print.
        p = "Loading" + "." * x       # Assign Loading and additional points to p.
        print (p, end = "\r")         # Prints p erasing the previous line.
        time.sleep(1)                 # Pauses the code 1 second for easier visualisation.
    print("   ")                      # String of space to immediately delete
    delete_last_lines()
