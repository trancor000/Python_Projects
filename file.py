
import sqlite3

conn = sqlite3.connect('files.db')

mycursor.execute("CREATE TABLE documents (txts VARCHAR(255))")

with conn:
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    txtList = ''
    for item in file_List:
        if item.endswith(".txt"):
            cur = conn.cursor()
            cur.execute("INSERT INTO documents(col_txts) VALUES (?)",
                        (item,))
            print(item)
    conn.commit()
conn.close()
