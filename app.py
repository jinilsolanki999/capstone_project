from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "registrations.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            course TEXT NOT NULL,
            event_name TEXT NOT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('full_name', '').strip()
    student_id = data.get('student_id', '').strip()
    course = data.get('course', '').strip()
    event_name = data.get('event_name', '').strip()

    if not all([full_name, student_id, course, event_name]):
        return jsonify({'success': False, 'message': 'All fields are required.'}), 400

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registrations (full_name, student_id, course, event_name) VALUES (?, ?, ?, ?)",
            (full_name, student_id, course, event_name)
        )
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': f'Successfully registered for {event_name}!'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Database error. Please try again.'}), 500

@app.route('/admin')
def admin():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrations ORDER BY registered_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return render_template('admin.html', registrations=rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)