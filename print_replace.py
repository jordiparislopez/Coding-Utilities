"""

    This file contains some utilities regarding printing.
    They are useful to manipulate prints and, in the ML context,
    to define interesting callbacks.

    The code will print "Loading" and introducing dots every second.
    Right after all the desired prints are in the output, the print shall
    erased.

"""


# Import time library
import time

# Initialise printing loop
for x in range (0,5):             # Maximum of 5 dots in the print.
    p = "Loading" + "." * x       # Assign Loading and additional points to p.
    print (p, end = "\r")         # Prints p erasing the previous line.
    time.sleep(1)                 # Pauses the code 1 second for easier visualisation.  
