import sqlite3

def get_db():
    conn = sqlite3.connect('app.db')
    return conn

def criar_tabela():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, nota TEXT)''')
    conn.commit()

def adicionar_nota(nota):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notas (nota) VALUES (?)', (nota,))
    conn.commit()

def listar_notas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas')
    return cursor.fetchall()