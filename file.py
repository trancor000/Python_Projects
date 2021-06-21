
import sqlite3

conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS documents (txts VARCHAR(255))")
    conn.commit
conn.close()

with conn:
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    txtList = ''
    for item in fileList:
        if item.endswith(".txt"):
            cur = conn.cursor()
            cur.execute("INSERT INTO documents(col_txts) VALUES (?)",
                        (item,))
            print(item)
    conn.commit()
conn.close()
