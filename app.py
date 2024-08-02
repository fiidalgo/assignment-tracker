import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully.")
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assignment_name TEXT NOT NULL,
        class_name TEXT NOT NULL,
        due_date TEXT NOT NULL
    )
    ''')
    print("Table created successfully.")

    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def insert_task():
    assignment_name = request.form['assignment_name']
    class_name = request.form['class_name']
    due_date = request.form['due_date']
    
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO tasks (assignment_name, class_name, due_date) VALUES (?, ?, ?)', 
                 (assignment_name, class_name, due_date))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    if request.method == 'POST':
        assignment_name = request.form['assignment_name']
        class_name = request.form['class_name']
        due_date = request.form['due_date']

        conn = sqlite3.connect('database.db')
        conn.execute('UPDATE tasks SET assignment_name = ?, class_name = ?, due_date = ? WHERE id = ?', 
                     (assignment_name, class_name, due_date, id))
        conn.commit()
        conn.close()

        return redirect('/')
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,))
    task = cursor.fetchone()
    conn.close()
    return render_template('update.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

init_sqlite_db()

if __name__ == '__main__':
    app.run(debug=True)