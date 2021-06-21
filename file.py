
import sqlite3

conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute(  # Creating the table in the db with its column
        "CREATE TABLE IF NOT EXISTS documents (txts VARCHAR(255))")
    conn.commit
conn.close()

conn = sqlite3.connect('files.db')
with conn:
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',  # defining the list for the files with its array
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    txtList = ''
    for item in fileList:
        # using a for loop to iterate specifically which items we want to use
        if item.endswith(".txt"):
            cur = conn.cursor()
            cur.execute("INSERT INTO documents(txts) VALUES (?)",
                        (item,))
            print(item)
    conn.commit()
conn.close()
