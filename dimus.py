import sqlite3 as sq
def convert_photo_by_name(name="default"):
    name+=".jpg"
    with open(name, 'rb') as file:
        photo=file.read()
    return photo
def set_photo(name="default"):
    photo=convert_photo_by_name(name)
    with sq.connect("uni.db") as con:
        cur=con.cursor()
        cur.execute("UPDATE students SET user_photo = :photo WHERE user_photo LIKE NULL",{'photo':photo})
#def student_card():
