import sqlite3
import csv

class Word:
    def __init__(self, word, meaning, level):
        self.word = word
        self.meaning = meaning
        self.level = level


def create_table():
    """Creates table if it doesn't exist"""
    connection = sqlite3.connect('words.db')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            meaning TEXT,
            level TEXT
        )
    """)

    connection.commit()
    connection.close()

def insert_word(word):
    """Inserts a word into the SQLite database"""
    connection = sqlite3.connect('words.db')
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO words (word, meaning, level) VALUES (?, ?, ?)",
        (word.word, word.meaning, word.level)
    )

    connection.commit()
    connection.close()

def load_words():
    """Loads words from the SQLite database"""
    words = []
    connection = sqlite3.connect('words.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM words")
    rows = cursor.fetchall()

    for row in rows:
        words.append(Word(row[1], row[2], row[3]))

    connection.close()
    return words

if __name__ == '__main__':
    create_table()
    # Populate the SQLite3 database from the CSV initially
    with open('words.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            word = Word(row[0], row[1], row[2])
            insert_word(word)