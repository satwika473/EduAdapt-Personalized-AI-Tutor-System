import sqlite3

def get_student_data(student_id):
    conn = sqlite3.connect('eduadapt.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    data = cursor.fetchone()
    conn.close()
    return data

def update_student_progress(student_id, progress_report):
    conn = sqlite3.connect('eduadapt.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET progress=? WHERE id=?", (str(progress_report), student_id))
    conn.commit()
    conn.close()