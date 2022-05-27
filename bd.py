import sqlite3 as sq

with sq.connect("uni.db") as con:

    cur = con.cursor()
    #cur.executescript("DROP TABLE IF EXISTS students")
    cur.executescript("""CREATE TABLE IF NOT EXISTS students (
    user_name TEXT NOT NULL,
    user_surname TEXT NOT NULL)
    """)

    cur.executescript("DROP TABLE IF EXISTS groups")
    cur.executescript("""CREATE TABLE IF NOT EXISTS groups (
    group_title TEXT NOT NULL)
    """)

    cur.executescript("DROP TABLE IF EXISTS group_members")
    cur.executescript("""CREATE TABLE IF NOT EXISTS group_members (
    user_name TEXT NOT NULL,
    user_surname TEXT NOT NULL,
    group_title TEXT NOT NULL,
    FOREIGN KEY (user_name) REFERENCES students (user_name),
    FOREIGN KEY (user_surname) REFERENCES students (user_surname),
    FOREIGN KEY (group_title) REFERENCES groups (group_title))
    """)


def students_add(a,b):
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_name = a
        user_surname = b
        cur.execute("INSERT INTO students (user_name, user_surname) VALUES (?,?)", (user_name, user_surname))



def groups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        group_title = input("Введите название группы: ")
        cur.execute("INSERT INTO groups (group_title) VALUES (?)", (group_title,))





def studgroups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_name1 = input("Введите имя студента: ")
        user_surname1 = input("Введите фамилию студента: ")
        group_title1 = input("Введите название группы, в которую хотите добавить студента: ")
        if cur.execute("SELECT 1 FROM groups WHERE group_title = :group", {"group": group_title1}).fetchone():
            if cur.execute("SELECT 1 FROM students WHERE user_name = :name", {"name": user_name1}).fetchone():
                if cur.execute("SELECT 1 FROM students WHERE user_surname = :surname", {"surname": user_surname1}).fetchone():
                    cur.execute("INSERT INTO group_members (group_title, user_name, user_surname) VALUES (?,?,?)", (group_title1, user_name1, user_surname1,))
                else:
                    print("ошибка")
                    exit(0)
            else:
                print("ошибкаи")
                exit(0)
        else:
            print("ошибка")
            exit(0)

