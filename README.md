# OddOnesOut

OddOnesOut is an open source command line tool. The main purpose of this program is to constantly check folders for files with specific extensions and move them to another folders.


# Installation

To install the latest stable version, run the following:
`pip install odd`

# Commands

1) Creating a process:

    `odd -c [FOLDER TO CHECK FOR FILES] [FOLDER TO MOVE FILES TO] [FILE EXTENSION]`

2) Stop a process:

    `odd -rm [PROCESS ID]`

3) Stop all processes:

    `odd -rm all`

4) Print a list of all process:

    `odd -ls`
