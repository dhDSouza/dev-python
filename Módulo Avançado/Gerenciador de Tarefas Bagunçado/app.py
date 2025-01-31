from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Criar banco de dados e tabela
conn = sqlite3.connect('tarefas.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, titulo TEXT)')
conn.commit()
conn.close()

# Rota para listar tarefas
@app.route('/', methods=['GET'])
def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = [{'id': row[0], 'titulo': row[1]} for row in cursor.fetchall()]
    conn.close()
    return render_template('index.html', tarefas=tarefas)

# Rota para adicionar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    data = request.json
    if 'titulo' in data:
        conn = sqlite3.connect('tarefas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tarefas (titulo) VALUES (?)', (data['titulo'],))
        conn.commit()
        conn.close()
        return jsonify({'mensagem': 'Tarefa adicionada com sucesso!'})
    return jsonify({'erro': 'Título é obrigatório'}), 400

# Rota para deletar uma tarefa
@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Tarefa removida com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
