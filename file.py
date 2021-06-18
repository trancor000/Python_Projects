
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
    cur=conn.cursor()
    cur.execute("SELECT col_texts FROM tbl_documents")
    varDocs=cur.fetchall()
    for item in varDocs:
        msg=r.varDocs
    print(msg)
