from .DAO import get_db

TABLE_NAME = 'authorize_data'


def create_database():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT NOT NULL, value\
        TEXT NOT NULL)''')
    print("table created")
    conn.commit()
    conn.close()
