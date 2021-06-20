
import sqlite3

conn = sqlite3.connect('files.db')


with conn:
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    txtList = ''
    for item in file_List:
        if item = txt.endswith(".txt"):
        cur = conn.cursor()
        cur.execute("INSERT INTO txtList(col_docs) VALUES (?)",
                    ('information.docx'))
        print(item)
