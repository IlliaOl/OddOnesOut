import os
import re
import shutil

"""------------------move_files--------------------------------
usage: moves files with specific extension to a specific folder
param: init_folder - initial folder
param: other_folder - folder to move files to
param: ext - extension of files
"""


def move_files(init_folder, other_folder, ext):
    while True:
        for entry in os.listdir(init_folder):
            if os.path.isfile(os.path.join(init_folder, entry)):
                if re.findall("\\." + ext, entry):
                    shutil.move(init_folder + "/" + entry, other_folder)


if __name__ == '__main__':
    move_files("D:/OddOnesOut_Folders/Folder_1", "D:/OddOnesOut_Folders/Folder_2", "txt")
