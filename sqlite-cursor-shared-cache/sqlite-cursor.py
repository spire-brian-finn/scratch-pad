import sqlite3

db1 = sqlite3.connect("file::memory:?cache=shared", uri=True)
db2 = sqlite3.connect("file::memory:?cache=shared", uri=True)

conn1 = db1.cursor()
conn2 = db2.cursor()
#conn2 = db1.cursor()

conn1.execute("CREATE TABLE leagues (id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL);")
conn1.execute("INSERT INTO leagues (name) VALUES ('A')")
conn1.execute("INSERT INTO leagues (name) VALUES ('B')")

#conn1.execute("UPDATE leagues SET name = name || '1'")
conn1.execute("UPDATE leagues SET name = name || '1' WHERE name = 'A';")
db1.commit()
print(f"conn1 rowcount: {conn1.rowcount}")
print(f"db1 total_changes: {db1.total_changes}")
# The next line will error out, since the db is locked by conn1
conn2.execute("UPDATE leagues SET name = name || '2'")
print(conn1.execute("SELECT * from leagues;"))