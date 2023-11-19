from flask import request, jsonify, Blueprint
from app import cache, authentication
from .DAO import get_db

exercise3_app = Blueprint('exercise3', __name__)

DATABASE_NAME = 'database.db'
TABLE_NAME = 'authorize_data'


@exercise3_app.route('/save', methods=['POST'], endpoint='save_data')
@authentication
def save_data():
    data = request.get_json()

    if 'key' not in data or 'value' not in data:
        return "Missing value"

    data_key, data_value = data['key'], data['value']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {TABLE_NAME} (key, value) VALUES (?, ?);", (data_key, data_value))
    conn.commit()
    conn.close()
    cache.clear()

    return "added successfully", 200


@exercise3_app.route('/get', methods=['GET'], endpoint='get_data')
@authentication
@cache.cached(timeout=60)
def get_key_details():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT key, value from {TABLE_NAME};")
    rows = cursor.fetchall()
    data = [{"key": row[0], "value": row[1]} for row in rows]
    conn.close()

    return jsonify(data)


@exercise3_app.route('/delete', methods=['POST'], endpoint='delete_data')
@authentication
def delete_data():
    data = request.get_json()
    if 'key' not in data:
        return 'Missing key'

    input_key = data['key']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE key = ?;', (input_key,))
    conn.commit()
    conn.close()
    cache.clear()
    return "Deleted successfully"
