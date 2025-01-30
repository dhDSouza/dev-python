from flask import Flask, request, redirect, url_for
from app.models.models import adicionar_nota, listar_notas
from app.views.views import mostrar_notas
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

@app.route('/')
def home():
    notas = listar_notas()
    return mostrar_notas(notas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nota = request.form['nota']
    adicionar_nota(nota)
    return redirect(url_for('home'))
