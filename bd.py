import sqlite3 as sq

with sq.connect("uni.db") as con:

    cur = con.cursor()
    cur.executescript("DROP TABLE IF EXISTS students")
    cur.executescript("""CREATE TABLE IF NOT EXISTS students (
    user_id INTEGER primary key AUTOINCREMENT,
    user_FIO TEXT NOT NULL,
    user_birthday INTEGER NOT NULL,
    user_photo BLOB)
    """)

    cur.executescript("DROP TABLE IF EXISTS groups")
    cur.executescript("""CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER primary key AUTOINCREMENT,
    group_title TEXT NOT NULL,
    group_faculty TEXT NOT NULL,
    group_amount INTEGER NOT NULL)
    """)

    cur.executescript("DROP TABLE IF EXISTS group_members")
    cur.executescript("""CREATE TABLE IF NOT EXISTS group_members (
    user_id INTEGER NOT NULL,
    group_title TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES students (user_id),
    FOREIGN KEY (group_title) REFERENCES groups (group_title))
    """)


def students_add(a,b,c):
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_FIO = a
        user_birthday = b
        cur.execute("INSERT INTO students (user_FIO, user_birthday) VALUES (?,?)", (user_FIO, user_birthday))


def groups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        group_title = input("Введите название группы: ")
        cur.execute("INSERT INTO groups (group_title) VALUES (?)", (group_title,))


def studgroups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_FIO = input("Введите ФИО студента, которого хотите добавить в группу: ")
        group_title1 = input("Введите название группы, в которую хотите добавить студента: ")
        if cur.execute("SELECT 1 FROM groups WHERE group_title = :group", {"group": group_title1}).fetchone():
            if cur.execute("SELECT 1 FROM students WHERE user_FIO = :FIO", {"FIO": user_FIO1}).fetchone():
                cur.execute("INSERT INTO group_members (group_title, user_FIO) VALUES (?,?)", (group_title1, user_FIO1,))
            else:
                print("ошибка")
                exit(0)
        else:
            print("ошибка")
            exit(0)
