# Spots2Cabrillo
A Python Converter: Skimmer Server's Spots.txt to Cabrillo

'''

SPOTS to CABRILLO Converter (s2c.py). (c) Jari Perkiömäki OH6BG

This Python script converts the Skimmer Server's Spots.txt data file
to CABRILLO, writing output to the corresponding CABRILLO file
(spots.log).

This script assumes that a Python 3 interpreter is installed on your computer.
Download the Python software at www.python.org; it's free.

HOW TO USE THIS SCRIPT

1. Place the Spots.txt file in a folder
2. Put this script into the same folder
3. Under *nix/Linux, make this script executable: chmod u+x s2c.py
4. Run at the command prompt: ./s2c.py &
5. Under Windows, double-clicking the icon of this file should launch
   the Python interpreter by file association, and run the script.
6. When done, the output file ("spots.log") can be found in the same folder.

12 Jul 2016: Moved to GitHub

10 Jul 2016. Added filtering of spots by CQ, CQ+DE, All; and by month and year

08 Jul 2016. Initial release (unpublished).

'''
