#!/usr/bin/python3
import subprocess
import argparse
import sqllite
import psutil
import sys


# Creating a command line arguments
my_parser = argparse.ArgumentParser(prog='odd',
                                    description='moves files with specific extension to a specific folder')
my_parser.add_argument('-c', action='store', type=str, nargs=3)
my_parser.add_argument('-rm', action='store', type=str, default="None")
my_parser.add_argument('-ls', action='store_true')

args = my_parser.parse_args()

# Creating a process
try:
    process = subprocess.Popen(["python", "checker.py", *args.c], stdout=subprocess.PIPE)
    identifier = sqllite.last_id()[0] + 1
    sqllite.insert_table(identifier, args.c[2], args.c[0], args.c[1], process.pid)
except FileNotFoundError:
    sys.stdout.write("Error: Folder not found")
    sys.exit()
except TypeError:
    pass
else:
    sys.stdout.write(f"ID of your process is {identifier}")


# removing a process
if args.rm == "None":
    pass
elif args.rm == "all":
    for process_record in sqllite.print_table():
        p = psutil.Process(process_record[-1])
        p.terminate()
        sqllite.remove_from_table(process_record[-1])
        sys.stdout.write(f"All processes has been removed")
else:
    try:
        process_id = sqllite.select_pid_table(args.rm)
        p = psutil.Process(process_id)
        p.terminate()
        sqllite.remove_from_table(process_id)
        sys.stdout.write(f"Process removed")
    except Exception:
        sys.stdout.write(f"Error: Wrong id")


"""------------------create_table--------------------------------
usage: prettifies the record from the table
record: a record from the table
"""


def prettify(record):
    record = str(record)
    record = record.replace("(", "|  ")
    record = record.replace(")", "|")
    record = record.replace(",", "  |")
    return record


# Printing a list of all current processes
if args.ls:
    for table_record in sqllite.print_table():
        try:
            psutil.Process(table_record[-1])
        except Exception:
            sqllite.remove_from_table(table_record[-1])
        else:
            print(prettify(table_record))
