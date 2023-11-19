import sqlite3

DATABASE_NAME = 'Database.db'
TABLE_NAME = 'authorize_data'


def get_db():
    db = sqlite3.connect(DATABASE_NAME)
    return db
