# -----------------------------------------------------------------------------
# Hello there! And welcome to the nightmare I call my code!
# Please, don't steal my code and claim it as your own, not that
# this is code that you would want to claim as your own
# © Patrick Brennan (AM2i9)
# https://github.com/AM2i9/DeskWiper
#-------------------------------------------------------------------------------

import os
import shutil
from pathlib import Path
import platform

# This part was implemented because I have both a windows and linux pc, but because 
# this program is only gonna support windows, its kinda useless
OS = platform.system()
seprator = ""

if OS == "Linux":
    seperator = "/"
if OS == "Windows":
    seperator = "\\"

# Automatically set to the directory of your desktop, so you don't have to do it yourself
directory = "{0}{1}Desktop{1}DeskWiper{1}".format(Path.home(),seperator)

def scan(directory): # Scans the selected directory and gets all unique file extensions

    file_extension_OUT = []

    desktop = os.listdir(directory)

    for file in desktop:

        if os.path.isfile(directory + seperator + file):

            # Python if statements are basically english. I mean, what other language checks
            # for a string in a list by using "not in"?
            if Path(directory + seperator + file).suffix not in file_extension_OUT:
                if Path(directory + seperator + file).suffix == "":
                    file_extension_OUT.append("No Extension")
                else:
                    file_extension_OUT.append(Path(directory + seperator + file).suffix)
        else:
            # Of course, directories don't have file extensions. So, if you want to move them, we have to
            # make some exceptions
            if "Directory" not in file_extension_OUT:
                file_extension_OUT.append("Directory")

    return file_extension_OUT

def moveFiles(directory, file_extensions, destinations): 
    # Its the function we've all been waiting for folks!
    # This is the function the ENTIRE program centers around
    
    try:
        desktop = os.listdir(directory)

        for file in desktop:
            filedir = directory+seperator+file
            suffix = ""
            
            # Checks to see if the file that it is moving is a file, then moves it to its selected location
            if os.path.isfile(filedir):
                if (suffix := Path(directory + seperator + file).suffix) == "":
                    suffix = "No Extension"
            else:
                # Directories don't have extensions
                suffix = "Directory"

            if suffix in file_extensions:

                if destinations[suffix]:
                    shutil.move(filedir,destinations[suffix] + seperator + file)
                
    # Welcome
        return True
    # To
    except:
    # Error
        return False
    # Handling
    