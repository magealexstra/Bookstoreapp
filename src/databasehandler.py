import sqlite3


def connect():
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()


def insert(title, author, year, isbn):
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
	conn.commit()
	conn.close()


def view():
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("SELECT * FROM book")
	results = curse.fetchall()
	conn.close()
	return results


def search(title="", author="", year="", isbn=""):
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
	results = curse.fetchall()
	conn.close()
	return results


def delete(ids):
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("DELETE FROM book WHERE id=?", (ids,))
	conn.commit()
	conn.close()


def update(ids, title, author, year, isbn,):
	conn = sqlite3.connect("books.db")
	curse = conn.cursor()
	curse.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, ids))
	conn.commit()
	conn.close()


connect()
# insert("Earthen ware", "jacks masson", 1960, 12345678932)
# delete(1)
# update(2, "Dirtworks", "jacks Johnson", 1900, 1234651132)
# print(view())
