
import sqlite3

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_ID INT\
        col_file TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_file) VALUES (?, ?, ?)",
                ('information.docx', ('Hello.txt', 'World.txt'), 'data.pdf'))
    conn.commit()
conn.close()


conn=sqlite3.connect('files.db')

with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_pictures( \
        ID STRING, \
        col_pics PNG, \
        col_sound MPG \
        col_jpg JPG \
        )")
    conn.commit()
conn.close()


conn=sqlite3.connect('files.db')

with conn:
    cur=conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_docs) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_documents(col_texts) VALUES (?, ?)", \
                ('Hello.txt', 'World.txt'))
    cur.execute("INSERT INTO tbl_documents(col_pdfs) VALUES (?)", \
                ('data.pdf'))
    conn.commit()
conn.close()

conn = sqlite3.connect('files.db')


with conn:
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for item in file_List:
        if item == txt.endswith(".txt")
    print(item)
