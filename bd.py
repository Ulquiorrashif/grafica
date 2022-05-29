import sqlite3 as sq

with sq.connect("uni.db") as con:

    cur = con.cursor()
    #cur.executescript("DROP TABLE IF EXISTS students")
    cur.executescript("""CREATE TABLE IF NOT EXISTS students (
    user_id INTEGER primary key AUTOINCREMENT,
    user_FIO TEXT NOT NULL,
    user_birthday TEXT NOT NULL,
    user_photo BLOB)
    """)

    #cur.executescript("DROP TABLE IF EXISTS groups")
    cur.executescript("""CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER primary key AUTOINCREMENT,
    group_title TEXT NOT NULL,
    group_faculty TEXT NOT NULL,
    group_amount INTEGER NOT NULL)
    """)

    #cur.executescript("DROP TABLE IF EXISTS group_members")
    cur.executescript("""CREATE TABLE IF NOT EXISTS group_members (
    user_id INTEGER NOT NULL,
    group_title TEXT NOT NULL)
    """)

    #cur.executescript("DROP TABLE IF EXISTS redact_group")
    cur.executescript("""CREATE TABLE IF NOT EXISTS redact_group (
    group_DO TEXT NOT NULL,
    group_POSLE TEXT NOT NULL)
    """)


def students_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_FIO = input("Введите ФИО студента, которого хотите отредактировать: ")
        user_birthday = input("Введите ДР студента, которого хотите отредактировать: ")
        cur.execute("INSERT INTO students (user_FIO, user_birthday) VALUES (?,?)", (user_FIO, user_birthday))
students_add()
def groups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        group_title = input("Введите название группы: ")
        group_faculty = input("Введите название кафедры, к которой прикреплена группа: ")
        cur.execute("INSERT INTO groups (group_title, group_faculty) VALUES (?,?)", (group_title,group_faculty,))



def studgroups_add():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_id = input("Введите номер зачётки студента: ")
        group_title = input("Введите название группы, в которую хотите добавить студента: ")
        if cur.execute("SELECT 1 FROM groups WHERE group_title = :group", {"group": group_title}).fetchone():
            if cur.execute("SELECT 1 FROM students WHERE user_id = :FIO", {"FIO": user_id}).fetchone():
                  cur.execute("INSERT INTO group_members (group_title, user_id) VALUES (?,?)", (group_title, user_id,))
                  cur.execute("UPDATE groups SET group_amount = group_amount + 1 WHERE group_title = ?", (group_title,))
            else:
                print("ошибка")
                exit(0)
        else:
            print("ошибка")
            exit(0)


studgroups_add()


def groups_output():
    with sq.connect("uni.db") as con:
        output = []
        cur = con.cursor()
        sqlite_select_query = """SELECT * from groups"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        for row in records:
            output.append(row[1])
        print(output)


groups_output()


# def students_redact():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         pre_user_FIO = input("Введите старое ФИО студента, которого хотите отредактировать: ")
#         pre_user_birthday = input("Введите старое ДР студента, которого хотите отредактировать: ")
#         post_user_FIO = input("Введите новое ФИО студента, которого хотите отредактировать: ")
#         post_user_birthday = input("Введите новое ДР студента, которого хотите отредактировать: ")
#         cur.execute("UPDATE students SET user_FIO = ? WHERE user_FIO = ?", (post_user_FIO, pre_user_FIO,))
#         cur.execute("UPDATE students SET user_birthday = ? WHERE user_birthday = ?", (post_user_birthday, pre_user_birthday,))
#         con.commit()


# students_redact()


# def groups_redact():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         group_title1 = input("Введите название группы, которую хотите отредактировать: ")
#         group_title2 = input("Введите новое название группы: ")
#         cur.execute("UPDATE groups SET group_title == ? WHERE group_title == ? ", (group_title2, group_title1,))
#         con.commit()
#         cur.execute("INSERT INTO redact_group (group_DO, group_POSLE) VALUES (?,?)", (group_title1,group_title2,))


# groups_redact()


# def students_delete():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         user_FIO1 = input("Введите ФИО студента, которого хотите удалить: ")
#         user_birthday1 = input("Введите ДР студента, которого хотите удалить: ")
#         cur.execute("DELETE FROM students WHERE user_FIO = ?", (user_FIO1,))
#         cur.execute("DELETE FROM students WHERE user_birthday = ?", (user_birthday1,))
#         con.commit()

# students_delete()

# def groups_delete():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         group_title1 = input("Введите название группы, которую хотите удалить: ")
#         cur.execute("DELETE FROM groups WHERE group_title = ?", (group_title1,))
#         con.commit()


# groups_delete()