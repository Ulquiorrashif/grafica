import sqlite3 as sq

with sq.connect("uni.db") as con:

    cur = con.cursor()
    # cur.executescript("DROP TABLE IF EXISTS students")
    cur.executescript("""CREATE TABLE IF NOT EXISTS students (
    user_id INTEGER primary key AUTOINCREMENT,
    user_FIO TEXT NOT NULL,
    user_birthday INTEGER NOT NULL,
    user_photo BLOB)
    """)

    # cur.executescript("DROP TABLE IF EXISTS groups")
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
    user_id INTEGER NOT NULL,
    group_DO TEXT NOT NULL,
    group_POSLE TEXT NOT NULL)
    """)


# def students_add():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         user_FIO = input("Введите ФИО студента, которого хотите отредактировать: ")
#         user_birthday = input("Введите ДР студента, которого хотите отредактировать: ")
#         cur.execute("INSERT INTO students (user_FIO, user_birthday) VALUES (?,?)", (user_FIO, user_birthday))
#
# def groups_add():
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         group_title = input("Введите название группы: ")
#         cur.execute("INSERT INTO groups (group_title) VALUES (?)", (group_title,))
#
# print("ТЕСТ РЕДАКТИРОВАНИЯ ")


def students_redact():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_id = input("Введите номер зачётки студента, которого хотите отредактировать: ")
        post_user_FIO = input("Введите новое ФИО студента, которого хотите отредактировать: ")
        post_user_birthday = input("Введите новое ДР студента, которого хотите отредактировать: ")
        cur.execute("UPDATE students SET user_FIO = ? WHERE user_id = ?", (post_user_FIO, user_id,))
        cur.execute("UPDATE students SET user_birthday = ? WHERE user_id = ?", (post_user_birthday, user_id,))
        con.commit()

#students_redact()


def students_move():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        user_id = input("Введите номер зачётки студента, которого хотите переместить в другую группу: ")
        group_title = input("Введите название группы, в которую хотите переместить студента: ")
        group_before = cur.execute("SELECT group_title FROM group_members WHERE user_id = :id", {"id": user_id}).fetchone()[0]
        print(group_before)
        cur.execute("UPDATE group_members SET group_title = ? WHERE user_id = ?", (group_title, user_id,))
        cur.execute("INSERT INTO redact_group (user_id, group_DO, group_POSLE) VALUES (?,?,?)", (user_id, group_before, group_title,))
        con.commit()
#students_move()


def groups_redact():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        group_title = input("Введите название группы, которую хотите переименовать: ")
        group_title_new = input("Введите новое название группы: ")
        cur.execute("UPDATE groups SET group_title = ? WHERE group_title == ? ", (group_title_new, group_title))
        cur.execute("UPDATE group_members SET group_title = ? WHERE group_title == ? ", (group_title_new, group_title))
        cur.execute("UPDATE redact_group SET group_DO = ? WHERE group_DO == ? ", (group_title_new, group_title))
        cur.execute("UPDATE redact_group SET group_POSLE = ?", (group_title_new,))
        con.commit()
groups_redact()

def students_delete():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        # user_FIO1 = input("Введите ФИО студента, которого хотите удалить: ")
        # user_birthday1 = input("Введите ДР студента, которого хотите удалить: ")
        user_id = input("Введите номер зачётки студента, которого хотите удалить: ")
        cur.execute("DELETE FROM students WHERE user_id == ?", (user_id,))
        con.commit()
#students_delete()



def groups_delete():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        group_title = input("Введите название группы, которую хотите удалить: ")
        cur.execute("DELETE FROM groups WHERE group_title = ?", (group_title,))
        con.commit()

#groups_delete()


# import sqlite3 as sq
#
#
#
#
# def students_add(a,b):
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         user_FIO =  a  # input("Введите ФИО студента, которого хотите отредактировать: ")
#         user_birthday = b#input("Введите ДР студента, которого хотите отредактировать: ")
#         cur.execute("INSERT INTO students (user_FIO, user_birthday) VALUES (?,?)", (user_FIO, user_birthday))
#
#
# def studgroups_add(a,b):
#     with sq.connect("uni.db") as con:
#         cur = con.cursor()
#         user_id = a #input("Введите номер зачётки студента: ")
#         group_title =b # input("Введите название группы, в которую хотите добавить студента: ")
#         if cur.execute("SELECT 1 FROM groups WHERE group_title = :group", {"group": group_title}).fetchone():
#             if cur.execute("SELECT 1 FROM students WHERE user_id = :FIO", {"FIO": user_id}).fetchone():
#                   cur.execute("INSERT INTO group_members (group_title, user_id) VALUES (?,?)", (group_title, user_id,))
#                   cur.execute("UPDATE groups SET group_amount = group_amount + 1 WHERE group_title = ?", (group_title,))
#             else:
#                 print("ошибка")
#                 exit(0)
#         else:
#             print("ошибка")
#             exit(0)
#studgroups_add(a,b)


# def groups_output():
#     with sq.connect("uni.db") as con:
#         output = []
#         cur = con.cursor()
#         sqlite_select_query = """SELECT * from groups"""
#         cur.execute(sqlite_select_query)
#         records = cur.fetchall()
#         for row in records:
#             output.append(row[1])
#         return output