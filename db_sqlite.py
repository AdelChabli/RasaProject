import sqlite3


def init_data():
    conn = sqlite3.connect('orientation.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''CREATE TABLE way(
    room VARCHAR,
    direction VARCHAR
  )'''
    cursor.execute(sql)

    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("ada", "Deuxième amphi situé dans le couloir à gauche, juste après l'amphitheatre Blaise."))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("blaise", "Premier amphitheatre situé dans le couloir à gauche."))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("cisco", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("elec", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("res", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("rob", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s1", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s2", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s3", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s4", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s5", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s6", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s7", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s8", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("s9", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 1", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 2", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 3", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 4", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 5", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 6", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 7", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 8", ""))
    cursor.execute('''INSERT INTO way(room,direction) VALUES (?, ?)''',
                   ("stat 9", ""))

    print("Table created successfully........")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


def select_data(room):
    conn = sqlite3.connect('orientation.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT direction FROM way WHERE room=?''', (room,))

    rows = cursor.fetchall()

    text = ""
    for row in rows:
        text = str(row)[2:-3]
        break

    # Closing the connection
    conn.close()

    return text;


def print_data():
    conn = sqlite3.connect('orientation.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM way''', )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    init_data()
    print("All data:")
    print_data()
    print("Select classique")
    print(select_data('blaise'))
