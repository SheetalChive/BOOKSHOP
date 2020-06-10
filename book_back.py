
import sqlite3

def create_teble():
    conn = sqlite3.connect("bookshop_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshop(id INTEGER PRIMARY KEY, book TEXT, author TEXT, year INTGER, isbn INTGER)")
    conn.commit()
    conn.close()

def insert(book,author,year,isbn):
    conn = sqlite3.connect("bookshop_db.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookshop VALUES(NULL,?,?,?,?)",(book,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("bookshop_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookshop")
    rows = cur.fetchall()
    conn.close()
    return rows

def update(book,author,year,isbn,id):
    conn = sqlite3.connect("bookshop_db.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookshop SET book = ? , author = ? , year = ? , isbn = ? WHERE id = ?",(book,author,year,isbn,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("bookshop_db.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bookshop WHERE id = ?" , (id,))
    conn.commit()
    conn.close()

create_teble()    
# insert('c','DennisRitchie',1972,100)
update('Let us C','YAshwant Kanetkar',2010,25365,2)
# delete(6)
# delete(3)




print(view())

    
