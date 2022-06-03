import sqlite3 as sq
import dimus as d
def Begin():
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        #cur.executescript("DROP TABLE IF EXISTS students")
        d.set_photo()
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
