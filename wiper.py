import os
import shutil
from pathlib import Path

directory = "C:\\Users\\Patrick\\Desktop\\DesktWiper\\testfolder\\"

def getDestinations(file_extensions):

    destinations_OUT = {}

    for extension in file_extensions:

        destinations_OUT[extension] = input("Enter the directory for {} files:".format(extension))
    
    return destinations_OUT


def scan(directory):

    file_extension_OUT = []

    desktop = os.listdir(directory)
    print(directory)

    for file in desktop:
        if os.path.isfile(directory + "\\" + file):

            if Path(directory + "\\" + file).suffix not in file_extension_OUT:
                if Path(directory + "\\" + file).suffix == "":
                    file_extension_OUT.append("NA")
                else:
                    file_extension_OUT.append(Path(directory + "\\" + file).suffix)
    
    return file_extension_OUT

def moveFiles(directory, file_extensions, destinations):
    
    desktop = os.listdir(directory)

    for file in desktop:
        if os.path.isfile(directory + file):
            fileName = str(file)

            splitFileName = fileName.split(".")

            try:
                fileEX = splitFileName[1]

                if destinations.get(fileEX):
                    shutil.move(directory + file, destinations.get(fileEX))

            except IndexError:

                if destinations.get("NA"):
                    shutil.move(directory + file, destinations.get("NA"))