import sqlite3
import json

conn = sqlite3.connect('/home/saad/Desktop/Full_stack_portfolio/Backend/db.sqlite3')
conn.row_factory = sqlite3.Row
c = conn.cursor()
try:
    c.execute("SELECT * FROM projects_project")
    rows = c.fetchall()
    print("Found", len(rows), "projects.")
    for row in rows:
        print(dict(row))
except Exception as e:
    print("Error:", e)
finally:
    conn.close()
