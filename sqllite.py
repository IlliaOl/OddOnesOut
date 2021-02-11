#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('processes.db')

c = conn.cursor()


"""------------------create_table--------------------------------
usage: creates a table in the database
"""


def create_table():
    c.execute("""CREATE TABLE process(
                idf INTEGER,
                ext text(10),
                init_folder text(40),
                other_folder text(40),
                pid INTEGER
        )""")

    conn.commit()


"""------------------insert_table--------------------------------
usage: insert values in the table
param: idf - id of the record in the table
param: ext - extension of the file
param: ini - initial folder
param: other - other folder
param: pid = id of the process
"""


def insert_table(idf, ext, ini, other, pid):
    c.execute(f"INSERT INTO process(idf, ext, init_folder, other_folder, pid) VALUES({idf}, '{ext}', '{ini}', '{other}'"
              f", {pid});")

    conn.commit()


"""------------------select_pid_table--------------------------------
usage: selects pid from the record with the specific id
param: id - id of the record in the table
"""


def select_pid_table(idf):
    c.execute(f"SELECT pid FROM process WHERE idf={idf}")

    pid = c.fetchone()

    conn.commit()

    return pid[0]


"""------------------last_id--------------------------------
usage: selects the id from the last record in the table
"""


def last_id():
    c.execute("SELECT idf FROM process WHERE idf = (SELECT MAX(idf) FROM process);")

    last = c.fetchone()
    conn.commit()

    if last is None:
        return 0,
    else:
        return last


"""------------------remove_from_table--------------------------------
usage: removes record fro the table with the specific process id
pid: pid - id of the process
"""


def remove_from_table(pid):
    c.execute(f"DELETE FROM process WHERE pid={pid};")

    conn.commit()


"""------------------print_table--------------------------------
usage: prints a whole table
"""


def print_table():
    c.execute(f"SELECT * FROM process")

    row = c.fetchall()

    conn.commit()
    return row
