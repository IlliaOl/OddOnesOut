import subprocess
import argparse
import psutil
import sys
import os


# TODO: add documentation

# TODO: add multiple processes

my_parser = argparse.ArgumentParser(prog='checker',
                                    description='moves files with specific extension to a specific folder')
my_parser.add_argument('-c', action='store', type=str, nargs=3)
my_parser.add_argument('-rm', action='store', type=str, default="None")

args = my_parser.parse_args()

try:
    subprocess.Popen(["python", "checker.py", *args.c], stdout=subprocess.PIPE)
except FileNotFoundError:
    sys.stdout.write("Error: Folder not found")
    sys.exit()
except TypeError:
    pass
else:
    sys.stdout.write("ID of your process is 1")


if args.rm != "None":
    os.system("taskkill /im python.exe /f")
