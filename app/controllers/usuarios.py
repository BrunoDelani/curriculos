from app import app
from flask import render_template
from app.models.tables import Usuario

@app.route('/usuarios')
def listar_usuarios():
    i = Usuario.query.all()
    return render_template('usuarios.html', usuario=i)