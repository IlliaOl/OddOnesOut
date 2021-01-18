import sqlite3

# TODO: Make better names

conn = sqlite3.connect('processes.db')

c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE process(
                idf INTEGER,
                ext text(10),
                init_folder text(40),
                other_folder text(40),
                pid INTEGER
        )""")

    conn.commit()


def insert_table(idf, ext, ini, other, pid):
    c.execute(f"INSERT INTO process(idf, ext, init_folder, other_folder, pid) VALUES({idf}, '{ext}', '{ini}', '{other}'"
              f", {pid});")

    conn.commit()


def select_pid_table(idf):
    c.execute(f"SELECT pid FROM process WHERE idf={idf}")

    pid = c.fetchone()

    conn.commit()

    return pid[0]


def last_id():
    c.execute("SELECT idf FROM process WHERE idf = (SELECT MAX(idf) FROM process);")

    last = c.fetchone()
    conn.commit()

    if last is None:
        return 0,
    else:
        return last


def remove_from_table(pident):
    c.execute(f"DELETE FROM process WHERE pid={pident};")

    conn.commit()


def print_table():
    c.execute(f"SELECT * FROM process")

    row = c.fetchall()

    conn.commit()
    for i in row:
        print(i)
