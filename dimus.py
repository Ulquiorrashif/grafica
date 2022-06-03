import sqlite3 as sq
import easygui as eg


def convert_photo_by_name(name="default.jpg"):
    with open(name, 'rb') as file:
        photo = file.read()
    return photo


def set_default_photo(id):
    photo = convert_photo_by_name()
    with sq.connect("uni.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE students SET user_photo = :photo WHERE user_id=:id", {'photo': photo,'id': id})
def set_custom_photo(id):
    photo=convert_photo_by_name(eg.fileopenbox(filetypes=["*.jpg"]))
    with sq.connect("uni.db") as con:
        cur=con.cursor()
        cur.execute("UPDATE students SET user_photo=:photo WHERE user_id=:id",{'photo': photo,'id': id})
# def student_card():
