import os
import re
import shutil
from sys import argv

# TODO: document code properly

"""------------------move_files--------------------------------
usage: moves files with specific extension to a specific folder
param: init_folder - initial folder
param: other_folder - folder to move files to
param: ext - extension of files
"""


# TODO: create terminal output

def move_files(init_folder, other_folder, ext):
    while True:
        for entry in os.listdir(init_folder):
            if os.path.isfile(os.path.join(init_folder, entry)):
                if re.findall("\\." + ext, entry):
                    shutil.move(init_folder + "/" + entry, other_folder)


move_files(argv[1], argv[2], argv[3])
