#!/usr/bin/python3
import subprocess
import argparse
import sqllite
import psutil
import signal
import sys
import os


# TODO: add documentation


my_parser = argparse.ArgumentParser(prog='checker',
                                    description='moves files with specific extension to a specific folder')
my_parser.add_argument('-c', action='store', type=str, nargs=3)
my_parser.add_argument('-rm', action='store', type=str, default="None")
my_parser.add_argument('-ls', action='store', type=str, default="None")

args = my_parser.parse_args()

try:
    proc = subprocess.Popen(["python", "checker.py", *args.c], stdout=subprocess.PIPE)
    ident = sqllite.last_id()[0] + 1
    sqllite.insert_table(ident, args.c[2], args.c[0], args.c[1], proc.pid)
except FileNotFoundError:
    sys.stdout.write("Error: Folder not found")
    sys.exit()
except TypeError:
    pass
else:
    sys.stdout.write(f"ID of your process is {ident}")

# TODO: check id

if args.rm != "None":
    pid = sqllite.select_pid_table(args.rm)
    p = psutil.Process(pid)
    p.terminate()
    sqllite.remove_from_table(pid)
    sys.stdout.write(f"Process removed")


if args.ls != "None":
    sqllite.print_table()