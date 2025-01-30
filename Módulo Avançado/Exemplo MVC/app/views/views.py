from flask import render_template

def mostrar_notas(notas):
    return render_template('notas.html', notas=notas)