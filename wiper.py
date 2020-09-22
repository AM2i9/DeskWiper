import os
import shutil
from pathlib import Path
import platform

OS = platform.system()
seprator = ""

if OS == "Linux":
    seperator = "/"
if OS == "Windows":
    seperator = "\\"

directory = "{0}{1}Desktop{1}DeskWiper{1}testfolder{1}".format(Path.home(),seperator)

def scan(directory):

    file_extension_OUT = []

    desktop = os.listdir(directory)
    print(directory)

    for file in desktop:
        if os.path.isfile(directory + seperator + file):

            if Path(directory + seperator + file).suffix not in file_extension_OUT:
                if Path(directory + seperator + file).suffix == "":
                    file_extension_OUT.append("No Extension")
                else:
                    file_extension_OUT.append(Path(directory + seperator + file).suffix)
        else:
            if "Directory" not in file_extension_OUT:
                file_extension_OUT.append("Directory")

    return file_extension_OUT

def moveFiles(directory, file_extensions, destinations):
    
    desktop = os.listdir(directory)

    for file in desktop:
        filedir = directory+seperator+file
        suffix = ""

        if os.path.isfile(filedir):
            if (suffix := Path(directory + seperator + file).suffix) == "":
                suffix = "No Extension"
        else:
            suffix = "Directory"

        if suffix in file_extensions:
            shutil.move(filedir,destinations[suffix] + seperator + file)